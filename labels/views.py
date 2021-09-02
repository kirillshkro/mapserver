from rest_framework import viewsets
from .models import PlacemarkModel, PlacemarkPhoto
from labels.serializers import PlacemarkSerializer, PlacemarkPhotoSerializer


# Create your views here.

class Placemarks(viewsets.ModelViewSet):
	queryset = PlacemarkModel.objects.all()
	serializer_class = PlacemarkSerializer

	def get_queryset(self):
		queryset = PlacemarkModel.objects.all()
		title = self.request.query_params.get('title')
		if title is not None:
			queryset = queryset.filter(title__icontains=title)
		return queryset


class PlacemarksPhoto(viewsets.ModelViewSet):
	queryset = PlacemarkPhoto.objects.all()
	serializer_class = PlacemarkPhotoSerializer

	def get_queryset(self):
		queryset = PlacemarkPhoto.objects.all()
		title = self.request.query_params.get('title')
		if title is not None:
			queryset = queryset.filter(title__icontains=title)
		return queryset
