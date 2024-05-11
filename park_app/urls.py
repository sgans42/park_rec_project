from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('parks/', views.parks, name='parks'),
    path('historical_sites/', views.historical, name="historical",),
    path('historical_innovation/', views.historical_innovation, name="historical_innovation", ),

    path('hunt/', views.hunt, name="hunt", ),
]
