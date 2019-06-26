from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('',views.home,name="homepage"),
	path('start/',views.start,name="startpage"),
	# path('viewattendance/',views.viewattendance,name="viewpage")
]