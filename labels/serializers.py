from rest_framework import serializers
from labels.models import PlacemarkModel, PlacemarkPhoto, Polygon


class PlacemarkSerializer(serializers.ModelSerializer):
	class Meta:
		model = PlacemarkModel
		fields = '__all__'


class PlacemarkPhotoSerializer(serializers.ModelSerializer):
	class Meta:
		model = PlacemarkPhoto
		fields = ('id', 'title', 'latitude', 'longitude', 'photo', 'polygon')

	def get_image_uri(self, obj):
		request = self.context['request']
		photo_url = obj.fingerprint.url
		return request.build_absolute_uri(photo_url)


class PolygonSerializer(serializers.ModelSerializer):
	color = serializers.ChoiceField(default=None, choices=Polygon.Colors)

	class Meta:
		model = Polygon
		fields = ('id', 'public_name', 'color')

	def create(self, validated_data):
		color = validated_data['color']
		if color is not None:
			color = (color + 1) % 3
		else:
			color = Polygon.Colors.RED
		validated_data['color'] = color
		return super(PolygonSerializer, self).create(validated_data)
