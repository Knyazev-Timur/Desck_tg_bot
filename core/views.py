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
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        login(request=request, user=user)
        return Response(serializer.data)


class ProfileView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = USER_MODEL.objects.all()
    pagination_class = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdatePasswordView(generics.UpdateAPIView):
    """ Редактирование пароля """
    model = User
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UpdatePasswordSerializer

    def get_object(self):
        return self.request.user