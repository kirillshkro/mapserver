from rest_framework import viewsets
from .models import PlacemarkModel, PlacemarkPhoto, Polygon
from labels.serializers import PlacemarkSerializer, PlacemarkPhotoSerializer
from labels.serializers import PolygonSerializer


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
		queryset = self.queryset
		title = self.request.query_params.get('title')
		if title is not None:
			queryset = queryset.filter(title__icontains=title)
		return queryset


class PolygonView(viewsets.ModelViewSet):
	queryset = Polygon.objects.all()
	serializer_class = PolygonSerializer

	def get_queryset(self):
		border = self.request.query_params.get('border')
		queryset = self.queryset
		if border is not None:
			queryset = queryset.filter(border__polygon=PlacemarkPhoto.polygon)
		return queryset

