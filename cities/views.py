from django.shortcuts import render
from django.views.generic import DetailView
from .models import City

# Create your views here.

class CitiesDetailView(DetailView):
    template_name = 'cities/city-detail.html'
    model = City
