from rest_framework import serializers, fields
from .models import PlacemarkModel, Coordinate


class PlacemarkSerializer(serializers.ModelSerializer):
	class Meta:
		model = PlacemarkModel
		fields = ('coordinate', 'title')


class CoordinateSerializer(serializers.Serializer):
	latitude = fields.FloatField(default=0.0)
	longitude = fields.FloatField(default=0.0)
	
	def create(self, validated_data):
		return Coordinate.objects.create(**validated_data)
	
	def update(self, instance, validated_data):
		instance.latitude = validated_data.get("latitude", instance)
		instance.longitude = validated_data.get("longitude", instance)
		if instance.is_valid():
			instance.save()
		return instance
