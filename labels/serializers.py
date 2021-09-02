from rest_framework import serializers

from .models import PlacemarkModel, PlacemarkPhoto


class PlacemarkSerializer(serializers.ModelSerializer):
	class Meta:
		model = PlacemarkModel
		fields = '__all__'


class PlacemarkPhotoSerializer(serializers.ModelSerializer):
	class Meta:
		model = PlacemarkPhoto
		fields = '__all__'

	def get_image_uri(self, obj):
		request = self.context['request']
		photo_url = obj.fingerprint.url
		return request.build_absolute_uri(photo_url)
