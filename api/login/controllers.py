from rest_framework import status, response, views, permissions
from login.serializers import LoginFormSerializer, UserSerializer
from django.contrib.auth import authenticate, login
from login.authentication import SessionAuthentication
from rest_framework.authentication import TokenAuthentication


class BaseLoggedInController:
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [
        permissions.IsAuthenticated
    ]


class LoginController(views.APIView):
    write_serializer_class = LoginFormSerializer
    read_serializer_class = UserSerializer

    def post(self, request):
        serializer = self.write_serializer_class(data=request.data)
        if not serializer.is_valid():
            return response.Response(data={'detail': serializer.errors['email']}, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(
            request,
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )
        if user is not None:
            login(request, user)
            read_serializer = self.read_serializer_class(instance=request.user)
            return response.Response(data=read_serializer.data)
        return response.Response(data={'detail': 'Invalid Credentials.'}, status=status.HTTP_403_FORBIDDEN)


class CurrentUserController(BaseLoggedInController, views.APIView):
    read_serializer_class = UserSerializer

    def get(self, request):
        serializer = self.read_serializer_class(instance=request.user)
        return response.Response(data=serializer.data)
