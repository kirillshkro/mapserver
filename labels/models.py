from django.db import models


class PlacemarkModel(models.Model):
	title = models.CharField(max_length=100, blank=False, unique=True)
	latitude = models.FloatField(default=0.0, blank=False)
	longitude = models.FloatField(default=0.0, blank=False)
	color = models.IntegerField(default=0)
