from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import login, get_user_model
from .models import Profile
# Create your views here.
User = get_user_model()


def guide(request):
    return render(request, 'guide/guide_page.html')


def instructions(request):
    return render(request, 'guide/instructions.html')


@login_required
def profile(request):
    return render(request, 'guide/profile.html')


def ranking(request):
    users = Profile.objects.all().order_by('-coins')
    context = {
        'users': users
    }
    return render(request, 'guide/ranking.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data.get('username'),
                                            email=form.cleaned_data.get(
                                                'email'),
                                            password=form.cleaned_data.get(
                                                'password1'))
            messages.success(
                request, r'Your account has been created!')
            login(request, user)
            return redirect('instructions')
    else:
        form = UserRegisterForm()
    return render(request, 'guide/register.html', {'form': form})


@login_required
def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, r'Your account has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'guide/profile_update.html', context)
