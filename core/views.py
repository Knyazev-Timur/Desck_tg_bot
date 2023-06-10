from django.contrib.auth import login, logout, get_user_model
from rest_framework import permissions, generics, status
from rest_framework.response import Response
from core.serializers import RegistrationSerializer, LoginSerializer, UserSerializer, UpdatePasswordSerializer
from core.models import User

USER_MODEL = get_user_model()


class RegistrationView(generics.CreateAPIView):
    model = USER_MODEL
    permissions_classes = [permissions.AllowAny]
    serializer_class = RegistrationSerializer


class LoginView(generics.GenericAPIView):
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

#####
# for MyPy def delete(self, request: Request, *args: Any, **kwargs: Any):
# Queryset -> queryset
#####
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