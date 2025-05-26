from django.db import models
from django.conf import settings

# Create your models here.
class RainfallList(models.Model):
    Title = models.CharField(null=False, max_length=100, default='')
    Location = models.CharField(null=False, max_length=100, default='')
    VolumeOfRunoff = models.CharField(null=False, max_length=100, default='')
    Precipitation = models.CharField(null=False, max_length=100, default='')
    Area = models.CharField(null=False, max_length=100, default='')
    SurfaceCoefficient = models.CharField(null=False, max_length=100, default='')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )