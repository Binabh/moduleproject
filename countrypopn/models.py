# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models


class NepalDistrict(models.Model):
    area_sq_km = models.FloatField()
    zone_name = models.CharField(max_length=50)
    dist_code = models.IntegerField()
    district = models.CharField(max_length=20)
    pop_total = models.IntegerField()
    pop_male = models.IntegerField()
    pop_female = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)


# Auto-generated `LayerMapping` dictionary for NepalDistrict model
nepaldistrict_mapping = {
    'area_sq_km': 'Area_sq_km',
    'zone_name': 'ZONE_NAME',
    'dist_code': 'DIST_CODE',
    'district': 'DISTRICT',
    'pop_total': 'pop_total',
    'pop_male': 'pop_male',
    'pop_female': 'pop_female',
    'geom': 'MULTIPOLYGON',
}