from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext, gettext_lazy as _
from .models import Profile
# from .models import Profile


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Придумайте имя пользователя")
    email = forms.EmailField(label="Электронная почта")
    password1 = forms.CharField(
        label=_("Пароль"),
        strip=False,
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label=_("Подтвердите пароль"),
        widget=forms.PasswordInput,
        strip=False
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(label="Имя пользователя")
    email = forms.EmailField(label="Электронная почта")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя")
    password = forms.CharField(
        label=("Пароль"),
        strip=False,
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = ('username', 'password')
