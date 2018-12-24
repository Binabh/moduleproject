# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models


class DistrictHeadquaters(models.Model):
    vdc_name = models.CharField(max_length=50)
    zone_name = models.CharField(max_length=16)
    region = models.CharField(max_length=16)
    dist_name = models.CharField(max_length=29)
    geom = models.PointField(srid=4326)


# Auto-generated `LayerMapping` dictionary for DistrictHeadquaters model
districtheadquaters_mapping = {
    'vdc_name': 'VDC_NAME',
    'zone_name': 'ZONE_NAME',
    'region': 'REGION',
    'dist_name': 'DIST_NAME',
    'geom': 'POINT',
}