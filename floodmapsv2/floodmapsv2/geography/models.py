#from django.db import models
from django.contrib.gis.db import models

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^django\.contrib\.gis"])


# Create your models here.

# Coast
class Coast(models.Model):
    attribute = models.CharField(max_length=5)
    style = models.CharField(max_length=255,blank=True,null=True)

    # geometry
    geometry = models.MultiPolygonField(srid=2157)
    objects = models.GeoManager() 
    
    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.attribute)
    class Meta:
        ordering = ['attribute']

# Province
class Province(models.Model):
    name = models.CharField(max_length=20)
    style = models.CharField(max_length=255,blank=True,null=True)
    area_sq_km = models.FloatField(blank=True,null=True)
    perimiter_km = models.FloatField(blank=True,null=True)

    # geometry
    geometry = models.MultiPolygonField(srid=2157)
    objects = models.GeoManager()

    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['name']


# County
class County(models.Model):
    name = models.CharField(max_length=40)
    irish_name = models.CharField(max_length=40)
    style = models.CharField(max_length=255,blank=True,null=True)

    # geometry
    geometry = models.MultiPolygonField(srid=2157)
    objects = models.GeoManager()

    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'counties'

# DED
class DistrictElectoralDivision(models.Model):
    name = models.CharField(max_length=40)
    county = models.ForeignKey(County)

    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['name']

# Town
class Town(models.Model):
    name = models.CharField(max_length=50)
    name_and_county = models.CharField(max_length=35)
    county = models.ForeignKey(County)
    centroid_x = models.FloatField()
    centroid_y = models.FloatField()
    irish_name = models.BooleanField()
    irish_class = models.CharField(max_length=30)
    town_category = models.IntegerField()
    source = models.CharField(max_length=25)

    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['name']

# Townland
class Townland(models.Model):
    name = models.CharField(max_length=50)
    os_townland_id = models.IntegerField()
    county = models.ForeignKey(County)
    ded = models.ForeignKey(DistrictElectoralDivision)
    upper = models.CharField(max_length=50)

    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['name']


# Coastal waters
class CoastalWater(models.Model):
    name = models.CharField(max_length=50)
    # coastal_area

    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['name']

# Catchments
class Catchment(models.Model):
    number = models.CharField(max_length=13) # EPA number
    name = models.CharField(max_length=40)
    style = models.CharField(max_length=255,blank=True,null=True)
    area_sq_km = models.FloatField(blank=True,null=True)
    perimiter_km = models.FloatField(blank=True,null=True)
    hydrometric_area = models.IntegerField()
    #rbd
    
    # geometry
    geometry = models.MultiPolygonField(srid=2157)
    objects = models.GeoManager()

    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['name','hydrometric_area']

# Roads
class Road(models.Model):
    mapflow_id = models.FloatField() # Mapflow ID
    name = models.CharField(max_length=50)
    approx_region = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    geosid = models.FloatField()
    nra_name = models.CharField(max_length=10)
    code = models.FloatField()
    fre = models.FloatField()
    approx_region_city_name = models.CharField(max_length=75)
    town = models.ForeignKey(Town)
    style = models.CharField(max_length=255,blank=True,null=True)
    # geometry
    geometry = models.MultiPolygonField(srid=2157)
    objects = models.GeoManager()

    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['name']

# Lakes
class Lake(models.Model):
    seg_cd = models.CharField(max_length=24) # EPA ref
    name = models.CharField(max_length=50)
    style = models.CharField(max_length=255,blank=True,null=True)
    area_sq_km = models.FloatField(blank=True,null=True)
    perimiter_km = models.FloatField(blank=True,null=True)
    hydrometric_area = models.IntegerField()
    #rbd
    
    # geometry
    geometry = models.MultiPolygonField(srid=2157)
    objects = models.GeoManager()

    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['name','hydrometric_area']

# Rivers
class River(models.Model):
    epa_code = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    style = models.CharField(max_length=255,blank=True,null=True)
    catchment = models.ForeignKey(Catchment)
    flow_direction = models.CharField(max_length=1)
    length = models.FloatField()
    up_stream_length = models.FloatField()
    down_stream_length = models.FloatField()

    # geometry
    geometry = models.MultiPolygonField(srid=2157)
    objects = models.GeoManager()

    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['name']
