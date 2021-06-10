from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import Friend
from .forms import FriendForm


# Create your views here.

def index(request):
	form = FriendForm()
	friends = Friend.objects.all()
	context = {"form": form, "friends": friends}
	return render(request, 'map_events/index.html', context=context)


def post(request):
	if request.is_ajax() and request.method == "POST":
		form = FriendForm(request.POST)
		if form.is_valid():
			instance = form.save()
			serializer_instance = serializers.serialize('json', [instance, ])
			response = {"instance": serializer_instance}
			return JsonResponse(response, status=200)
		else:
			errors = {"error": form.errors}
			return JsonResponse(errors, status=400)
	return JsonResponse({"error": ""}, status=400)
