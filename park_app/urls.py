from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('parks/', views.parks, name='parks'),
    path('parks_chuck/', views.parks_chuck, name='parks_chuck'),
    path('historical_sites/', views.historical, name="historical",),

    path('historical_innovation/', views.historical_innovation, name="historical_innovation", ),

    path('hunt/', views.hunt, name="hunt", ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
