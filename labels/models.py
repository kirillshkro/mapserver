from django.db import models


class PlacemarkModel(models.Model):
	title = models.CharField(max_length=200, blank=False, unique=True)
	latitude = models.FloatField(default=0.0, blank=False)
	longitude = models.FloatField(default=0.0, blank=False)


class PlacemarkPhoto(PlacemarkModel):
	photo = models.ImageField(verbose_name='Фото', upload_to='images/', width_field='width_photo',
	                          height_field='height_photo')
	width_photo = models.PositiveIntegerField(blank=True)
	height_photo = models.PositiveIntegerField(blank=True)
