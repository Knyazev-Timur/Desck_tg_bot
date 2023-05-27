from django.shortcuts import render
from django.contrib.auth import get_user_model, login, logout
from rest_framework import generics, status, permissions
from rest_framework.response import Response

from core.serializers import RegistrationSerilazer, LoginSerilazer, UpdatePasswordSerilazer, UserSerilazer

USER_MODEL = get_user_model()


class RegistrationView(generics.CreateAPIView):
    model = USER_MODEL
    permissions_classes = [permissions.AllowAny]
    serializer_class = RegistrationSerilazer

class LoginView(generics.CreateAPIView):

    serializer_class = LoginSerilazer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        login(request=request, user=user)
        return Response(serializer.data)
