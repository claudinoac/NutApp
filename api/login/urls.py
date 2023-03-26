from login.controllers import LoginController, CurrentUserController
from django.urls import path

urlpatterns = [
    path('', LoginController.as_view()),
    path('me', CurrentUserController.as_view()),
]
