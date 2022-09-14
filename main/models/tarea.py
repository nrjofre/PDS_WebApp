from django.db import models

class Tarea(models.Model):
    name = models.CharField(max_length=20)
    statement = models.TextField(max_length=1000, blank=True)
    image = models.ImageField(blank=True, upload_to="images/")

    def __str__(self):
        return str(self.name)