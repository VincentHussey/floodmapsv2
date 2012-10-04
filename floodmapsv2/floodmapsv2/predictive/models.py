from django.contrib.gis.db import models

# Create your models here.
# PFRA

class AreaOfSignificantPotentialRisk(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255,null=True,blank=True)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now=True)
    
    # geometry
    geometry = models.MultiPolygonField(srid=2157)
    objects = models.GeoManager()
    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['name']   
        verbose_name_plural = 'areas of significant potential risk'
        
# Predictive Floods
# predictive flood polygons
class ClimateScenario(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255,null=True,blank=True)
    acronym = models.CharField(max_length=10) 
    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['name']

class AnnualExceedanceProbabilityScenario(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255,null=True,blank=True)
    acronym = models.CharField(max_length=10)
    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['name']

class PredictiveSource(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255,null=True,blank=True)
    acronym = models.CharField(max_length=10)
    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['name']

class PredictiveScenario(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255,null=True,blank=True)
    climate_scenario = models.ForeignKey(ClimateScenario)
    annual_exceedance_probability_scenario = models.ForeignKey(AnnualExceedanceProbabilityScenario)
    acronym = models.CharField(max_length=10)
    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['name']

class PredictiveUncertaintyBand(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255,null=True,blank=True)
    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['name']

class PredictiveFloodModel(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255,null=True,blank=True)
    acronym = models.CharField(max_length=10)
    scenario = models.ForeignKey(PredictiveScenario)
    source = models.ForeignKey(PredictiveSource)
    aspr = models.ForeignKey(AreaOfSignificantPotentialRisk)
    # survey
    # hydrology
    # boundary_condition
    # validation
    
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now=True)
    
    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['name']
          
class PredictiveFloodModelPoint(models.Model):
    parent = models.ForeignKey(PredictiveFloodModel)    
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now=True)
    #elevation
    #flow
    #velocity
    #depth
    
    # geometry
    geometry = models.PointField(srid=2157)
    objects = models.GeoManager()
    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.parent)
    class Meta:
        ordering = ['parent'] 

class PredictiveFloodExtent(models.Model):
    parent = models.ForeignKey(PredictiveFloodModel)
    
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now=True)
    # geometry
    geometry = models.PolygonField(srid=2157)
    objects = models.GeoManager()
    
    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.parent)
    class Meta:
        ordering = ['parent']
    
class PredictiveFloodExtentUncertainty(models.Model):
    parent = models.ForeignKey(PredictiveFloodModel)
    uncertainty_band = models.ForeignKey(PredictiveUncertaintyBand)
    
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now=True)
    # geometry
    geometry = models.MultiLineStringField(srid=2157)
    objects = models.GeoManager()
    
    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.parent)
    class Meta:
        ordering = ['parent']
        verbose_name_plural = 'predictive flood extent uncertainties'

# predictive flood depth (grid?)

# predictive flood velocity (grid?)

# predictive flood risk (grid?)
