from django.db import models


class Davlat(models.Model):
    name = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)
    poytaxt = models.CharField(max_length=200, default=None)
    region_count = 0


class Region(models.Model):
    country = models.ForeignKey(Davlat, on_delete=models.RESTRICT, default=None)
    name = models.CharField(max_length=100)
