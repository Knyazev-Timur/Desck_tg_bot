from django.contrib.auth import login, logout, get_user_model
from rest_framework import permissions, generics, status
# from rest_framework.generics import (
#     CreateAPIView,
#     GenericAPIView,
#     RetrieveUpdateDestroyAPIView,
#     UpdateAPIView,
# )
from rest_framework.response import Response
from core.serializers import RegistrationSerializer, LoginSerializer, UserSerializer, UpdatePasswordSerializer

from core.models import User
# from core.serializers import CreateUserSerializer

# from core.serializers import (
#     CreateUserSerializer,
#     LoginSerializer,
#     UserSerializer,
#     UpdatePasswordSerializer, RegistrationSerializer,
# )


USER_MODEL = get_user_model()

# class SignupView(generics.CreateAPIView):
#     """ Вход для пользователя """
#     model = User
#     permission_classes = [permissions.AllowAny]
#     serializer_class = CreateUserSerializer
#
#     def perform_create(self, serializer):
#         super().perform_create(serializer)
#         login(
#             self.request,
#             user=serializer.user,
#             backend="django.contrib.auth.backends.ModelBackend",
#         )

class RegistrationView(generics.CreateAPIView):
    model = USER_MODEL
    permissions_classes = [permissions.AllowAny]
    serializer_class = RegistrationSerializer

class LoginView(generics.GenericAPIView):
    """ Авторизация пользователя """
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        s: LoginSerializer = self.get_serializer(data=request.data)
        s.is_valid(raise_exception=True)
        user = s.validated_data["user"]
        login(request, user=user)
        user_serializer = UserSerializer(instance=user)
        return Response(user_serializer.data)


class ProfileView(generics.RetrieveUpdateDestroyAPIView):
    """ Профиль пользователя """
    model = User
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response({})


class UpdatePasswordView(generics.UpdateAPIView):
    """ Редактирование пароля """
    model = User
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UpdatePasswordSerializer

    def get_object(self):
        return self.request.user