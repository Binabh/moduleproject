# Register your models here.

from django.contrib.gis import admin
from .models import City
from leaflet.admin import LeafletGeoAdmin


class CityAdmin(LeafletGeoAdmin):
    # fields to show in admin listview
    list_display = ('name', 'geometry')


# register models in the admin site
admin.site.register(City, CityAdmin)
