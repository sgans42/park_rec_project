from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'park_app/home.html')


def parks_view(request):
    return render(request, 'park_app/parks.html')

