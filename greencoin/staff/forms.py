from guide.models import Profile
from django import forms
from django.contrib.auth.models import User
from .models import Trash


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('coins',)


class TrashAddForm(forms.ModelForm):
    class Meta:
        model = Trash
        fields = ('trash_type', 'weight')
