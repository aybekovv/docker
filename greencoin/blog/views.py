from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.db.models import Q
from django.forms import inlineformset_factory
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin)

from braces.views import SuperuserRequiredMixin

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, PostImage
from .forms import *

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'object_list'
    ordering = ['-date_posted']

    def get_queryset(self, *args, **kwargs):
        qs = Post.objects.all().order_by('-id')
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query)
            )
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        return context


class PostDetailView(DetailView):
    model = Post


def create_post(request):
    form = PostForm(request.POST or None)
    title = 'Create a Post'
    PostImageFormSet = inlineformset_factory(Post, PostImage, form=PostImageForm, extra=1, can_delete=True)
    if request.method == 'POST':
        if form.is_valid():
            post = form.save()
            formset = PostImageFormSet(request.POST, request.FILES, instance=post)
            if formset.is_valid():
                formset.save()
            return redirect(post.get_absolute_url())
    formset = PostImageFormSet()
    return render(request, 'blog/post_create_form.html', locals())


class PostUpdateView(SuperuserRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']


class PostDeleteView(SuperuserRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("blog:home")
