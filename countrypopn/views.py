from django.shortcuts import render
import json
from .models import NepalDistrict
from django.core.serializers import serialize

# Create your views here.

def PopulationView(request):
    my_geo_json = serialize('geojson', NepalDistrict.objects.all(), geometry_field='geom', fields=('area_sq_km','zone_name','dist_code','district','pop_total','pop_male','pop_female',))
    new_my_geo_json = json.loads(my_geo_json)
    new_my_geo_json.pop('crs', None)

    return render(request,'countrypopn/popn_map.html', {'my_geo_json': json.dumps(new_my_geo_json)})
