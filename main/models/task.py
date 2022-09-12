from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=20)
    stage = models.TextField(max_length=1000, blank=True)


    def __str__(self):
        return str(self.name)