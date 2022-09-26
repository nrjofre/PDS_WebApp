from django.db import models
from main.models.tarea import Tarea

class Task(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE, related_name="DCL", null=True)
    name = models.CharField(max_length=20)
    stage = models.TextField(max_length=1000, blank=True)


    def __str__(self):
        return str(self.name)