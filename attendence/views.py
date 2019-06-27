from django.shortcuts import render

def home(request):
	return render(request, 'mainattendance/home.html')
