from django.db import models


class Command(models.Model):
    commandString = models.CharField(max_length=100)
    sendCommand = models.BooleanField()

    def __str__(self):
        return f"Command: {self.commandString}, Send: {self.sendCommand}"
