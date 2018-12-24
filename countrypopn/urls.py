from django.urls import path, include
from . import views

urlpatterns = [
    # city detail view
    path('',views.PopulationView),
]