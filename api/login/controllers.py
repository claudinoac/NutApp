from rest_framework import status, response, views, permissions
from login.serializers import LoginSerializer
from django.contrib.auth import authenticate, login
from login.authentication import SessionAuthentication
from rest_framework.authentication import TokenAuthentication


class LoginController(views.APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return response.Response(data={'detail': serializer.errors['email']}, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(
            request,
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )
        if user is not None:
            login(request, user)
            return response.Response(data={'detail': 'Logged In.'})
        return response.Response(data={'detail': 'Invalid Credentials.'}, status=status.HTTP_403_FORBIDDEN)


class BaseLoggedInController:
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [
        permissions.IsAuthenticated
    ]
