from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Hora(models.Model):
    hora = models.CharField(max_length=120)
    especialidad = models.TextField()
    publicada_en = models.DateTimeField(default=timezone.now)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.hora

    class Meta:
        ordering = ['-publicada_en']
