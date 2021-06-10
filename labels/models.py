from django.db import models


class Coordinate(models.Model):
	latitude = models.FloatField(default=0.0, null=False)
	longitude = models.FloatField(default=0.0, null=False)


class PlacemarkModel(models.Model):
	title = models.CharField(max_length=100, null=False)
	coordinate = models.OneToOneField(Coordinate, on_delete=models.CASCADE)
