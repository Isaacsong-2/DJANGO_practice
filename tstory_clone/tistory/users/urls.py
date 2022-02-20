from django.urls import URLPattern, re_path, path

from .views import register

urlpattern = [
    path('register/', register, name='register'),
]
