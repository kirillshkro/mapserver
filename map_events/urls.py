from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('post/ajax/friend', views.post, name='post')
]
