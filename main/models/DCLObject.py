from django.db import models

class Figure(models.Model):
    CATEGORY = ('Bar', 'Support', 'SSupport', 'BallJoint', 'ConnectingRod','Embedment', 'Force')

    category = models.CharField(max_length=100, null=True, choices=CATEGORY)
    