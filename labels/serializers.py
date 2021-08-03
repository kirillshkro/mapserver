from rest_framework import serializers

from .models import PlacemarkModel


class PlacemarkSerializer(serializers.ModelSerializer):
	class Meta:
		model = PlacemarkModel
		fields = '__all__'
