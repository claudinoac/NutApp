from login.controllers import LoginController
from django.urls import path

urlpatterns = [
    path('', LoginController.as_view()),
]
