from django import forms
from .models import PlacemarkModel, Coordinate


class CoordinateForm(forms.ModelForm):
	class Meta:
		model = Coordinate
		fields = ['latitude', 'longitude']


class PlacemarkSendForm(forms.ModelForm):
	class Meta:
		model = PlacemarkModel
		fields = ['title', 'coordinate']
