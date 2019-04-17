from .models import *
from django import forms
from django.forms.models import inlineformset_factory

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content',]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }


class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ['image', ]
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

