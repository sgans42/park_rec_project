from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'park_app/home.html')

def parks(request):
    return render(request, 'park_app/parks.html')


def parks_chuck(request):
    return render(request, 'park_app/parks_chuck.html')

def historical(request):
    return render(request, 'park_app/historical.html')

def historical_innovation(request):
    return render(request, 'park_app/historical_innovation.html')

def hunt(request):
    return render(request, 'park_app/hunt.html')



