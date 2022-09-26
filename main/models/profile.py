from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile", null=True)
    score = models.IntegerField(default=0)

    apoyo_deslizante = models.IntegerField(default=0)
    apoyo_fijo = models.IntegerField(default=0)
    empotramiento = models.IntegerField(default=0)
    rotula = models.IntegerField(default=0)
    viela = models.IntegerField(default=0)
    fuerza_distribuida = models.IntegerField(default=0)
    fuerza_angular = models.IntegerField(default=0)