from django.db import models
from django.contrib.auth.models import User

STAGE_CHOICES = [(1,'1'), (2,'2'), (3,'3'), (4,'4')]

class Tarea(models.Model):
    name = models.CharField(max_length=20)
    statement = models.TextField(max_length=1000)
    image = models.ImageField(blank=True, upload_to="images/")
    starting_stage = models.IntegerField(choices=STAGE_CHOICES, default=1)
    difficulty = models.IntegerField(default=1)

    apoyo_deslizante = models.IntegerField(default=0)
    apoyo_fijo = models.IntegerField(default=0)
    empotramiento = models.IntegerField(default=0)
    rotula = models.IntegerField(default=0)
    biela = models.IntegerField(default=0)
    fuerza_distribuida = models.IntegerField(default=0)
    fuerza_angular = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    

    def __str__(self):
        return str(self.name)