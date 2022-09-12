from django.db import models


class DCL(models.Model):
    

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)