from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showIndex),
    path('cities/', include('cities.urls')),
    path('disthq/', include('disthq.urls')),
    path('countrypopn/', include('countrypopn.urls')),
]
