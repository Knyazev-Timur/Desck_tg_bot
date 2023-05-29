from django.contrib import admin
from django.urls import path

from core import views
from core.views import RegistrationView, LoginView, ProfileView, UpdatePasswordView

urlpatterns = [
    path('signup', views.RegistrationView.as_view, name='sign-up'),
    path('login', views.LoginView.as_view, name='login'),
    path('profile', views.ProfileView.as_view, name='profile'),
    path('update_password', views.UpdatePasswordView.as_view, name='update_password'),
]
