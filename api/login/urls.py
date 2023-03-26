from login.controllers import LoginController, CurrentUserController, LogoutController
from django.urls import path

urlpatterns = [
    path('', LoginController.as_view()),
    path('me', CurrentUserController.as_view()),
    path('logout', LogoutController.as_view()),
]
