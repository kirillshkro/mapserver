import random
from django.shortcuts import render
from rest_framework import viewsets
from .models import PlacemarkModel, Coordinate
from labels.serializers import PlacemarkSerializer, CoordinateSerializer


# Create your views here.

def index(request):
	placemarks = PlacemarkModel.objects.all()
	context = {"placemarks": placemarks}
	return render(request, "labels/index.html", context)


class PlacemarkIndex(viewsets.ModelViewSet):
	queryset = PlacemarkModel.objects.all()
	serializer_class = PlacemarkSerializer


class CoordinatesIndex(viewsets.ModelViewSet):
	queryset = Coordinate.objects.all()
	serializer_class = CoordinateSerializer
