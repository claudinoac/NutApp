from consultation.models import Consultation
from django.db.models import Q


class ConsultationError(Exception):
    pass


class ConsultationService():
    def __init__(self):
        pass

    def create_consultation(self, patient, professional, date_from, date_to):
        if date_from >= date_to:
            raise ConsultationError({
                "error_code": "invalid_date_range",
                "detail": "Hora de início da consulta não pode ser maior que data de finalização"
            })

        if professional.consultation_set.filter(
            Q(date_from__lte=date_from, date_to__gte=date_from)
            | Q(date_from__gte=date_from, date_to__gte=date_to)
            | Q(date_from__gte=date_from, date_to__lte=date_to)
        ).exists():
            raise ConsultationError({
                "error_code": "consultation_schedule_collision",
                "detail": "Horário da consulta colide com uma ou mais consultas desse profissional"
            })
        return Consultation.objects.create(
            patient=patient, professional=professional, date_from=date_from, date_to=date_to
        )
