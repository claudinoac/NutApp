from django.db import models


class Nutritionist(models.Model):
    user = models.OneToOneField(to="auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
