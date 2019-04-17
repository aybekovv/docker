from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from .forms import LoginForm
from .views import (guide,
                    register,
                    instructions,
                    profile,
                    profile_update,
                    ranking)


urlpatterns = [
    path('', guide, name='guide-page'),
    path('register/', register, name='register-page'),
    path('ranking/', ranking, name='ranking'),
    path('login/', auth_views.LoginView.as_view(form_class=LoginForm, template_name='guide/login.html'),
         name='login-page'),
    path('logout/', auth_views.LogoutView.as_view(template_name='guide/guide_page.html'),
         name='logout'),
    path('instructions/', instructions, name='instructions'),
    path('profile/', profile, name='profile'),
    path('profile-update/', profile_update, name='profile-update'),
]
