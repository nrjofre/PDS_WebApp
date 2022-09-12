from django.db import models


class DCL(models.Model):
    models.ForeignKey()

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)