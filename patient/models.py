from django.db import models


class Patient(models.Model):
    user = models.OneToOneField(to="auth.User", on_delete=models.CASCADE)
    nutritionist = models.ForeignKey(to="nutritionist.Nutritionist", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
