from django.db import models


class Consultation(models.Model):
    patient = models.ForeignKey(to="patient.Patient", on_delete=models.SET_NULL, null=True)
    professional = models.ForeignKey(to="nutritionist.Nutritionist", on_delete=models.SET_NULL, null=True)
    is_confirmed = models.BooleanField(default=False)
    is_finished = models.BooleanField(default=False)
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()

    def __str__(self):
        return f"Consultation: {self.professional} - {self.patient} - {self.date_from} to {self.date_to}"
