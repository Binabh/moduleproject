from django.urls import path, include
from . import views

urlpatterns = [
    # city detail view
    path('city/<slug:pk>',views.CitiesDetailView.as_view(), name='city-detail'),
]