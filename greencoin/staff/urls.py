from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include, re_path
import re
from .views import *


urlpatterns = [

    path('', staff_view, name='staff-page-url'),
    path('statistics/', trash_statistics, name='statistics'),
    re_path(r'(?P<name>[\w|\W]+)', coins_view, name='coins-page-url'),

]
