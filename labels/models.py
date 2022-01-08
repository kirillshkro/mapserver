from django.db import models
from uuid import uuid4


class PlacemarkModel(models.Model):
    title = models.CharField(max_length=200, blank=False, unique=True)
    latitude = models.FloatField(default=0.0, blank=False)
    longitude = models.FloatField(default=0.0, blank=False)


class PlacemarkPhoto(PlacemarkModel):
    photo = models.ImageField(verbose_name='Фото', upload_to='images/', width_field='width_photo',
                              height_field='height_photo', null=True)
    width_photo = models.PositiveIntegerField(null=True)
    height_photo = models.PositiveIntegerField(null=True)
    polygon = models.ForeignKey('Polygon', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Polygon(models.Model):
    class Colors(models.TextChoices):
        RED = "#ff0000"
        YELLOW = "#ffff00"
        GREEN = "#00ff00"

    color = models.CharField(max_length=50, choices=Colors.choices, default=Colors.RED)
    opacity = models.FloatField(default=0.75)
    border_opacity = models.FloatField(default=0.5)
    private_id = models.UUIDField(default=uuid4(), unique=True)
    public_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.public_name
