from django.db import models
from django.contrib.auth.models import User

DIFICULTY_CHOICES = [(1,'1'), (2,'2'), (3,'3')]
STAGE_CHOICES = [(1,'1'), (2,'2'), (3,'3'), (4,'4')]

class Tarea(models.Model):
    name = models.CharField(max_length=20)
    statement = models.TextField(max_length=1000)
    image = models.ImageField(blank=True, upload_to="images/")
    starting_stage = models.IntegerField(choices=STAGE_CHOICES, default=1)
    difficulty = models.IntegerField(choices=DIFICULTY_CHOICES, default=1)
    categories = {}
    score = 0
    

    def __str__(self):
        return str(self.name)