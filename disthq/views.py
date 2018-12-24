from django.shortcuts import render
import json
from .models import DistrictHeadquaters
from django.core.serializers import serialize

# Create your views here.

def HeadquatersView(request):
    my_geo_json = serialize('geojson', DistrictHeadquaters.objects.all(), geometry_field='geom', fields=('vdc_name','zone_name','region','dist_name',))
    new_my_geo_json = json.loads(my_geo_json)
    new_my_geo_json.pop('crs', None)

    return render(request,'disthq/disthqs.html', {'my_geo_json': json.dumps(new_my_geo_json)})
