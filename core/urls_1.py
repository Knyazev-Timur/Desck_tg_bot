"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from core import views

urlpatterns = [
    path('signup', views.RegistrationView.as_view(), name='signup'),
    path('login', views.LoginView.as_view(), name='login'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('update_password', views.UpdatePasswordView.as_view(), name='update_password'),
]


# from django.urls import path
#
# from core import views
#
# urlpatterns = [
#     path("signup", views.SignupView.as_view()),
#     path('regup', views.RegistrationView.as_view, name='signup'),
#     path("login", views.LoginView.as_view()),
#     path("profile", views.ProfileView.as_view()),
#     path("update_password", views.UpdatePasswordView.as_view()),
# ]
