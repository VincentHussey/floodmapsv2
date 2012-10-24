from django.contrib.gis.db import models

# Create your models here.
# PFRA
class Status(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255,null=True,blank=True)
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['name']   
        verbose_name_plural = 'status'

class VersionType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255,null=True,blank=True)
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['name']

class Availability(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255,null=True,blank=True)
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'availability'

class UnitOfManagement(models.Model):
    name = models.CharField(max_length=50)
    rbd = models.BooleanField(default=True)
    acronym = models.CharField(max_length=10) 
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['name']   
        verbose_name_plural = 'units of management'
        
class AreaOfPotentialSignificantRisk(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255,null=True,blank=True)
    uom = models.ForeignKey(UnitOfManagement)
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
        verbose_name_plural = 'areas of potential significant risk'
        
class Climate(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255,null=True,blank=True)
    acronym = models.CharField(max_length=10) 
    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['name']

class AnnualExceedanceProbability(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255,null=True,blank=True)
    acronym = models.CharField(max_length=10)
    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'annual exceedance probabilities'

class Source(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255,null=True,blank=True)
    acronym = models.CharField(max_length=10)
    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['name']

class Scenario(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255,null=True,blank=True)
    climate = models.ForeignKey(Climate)
    aep = models.ForeignKey(AnnualExceedanceProbability)
    source = models.ForeignKey(Source)
    acronym = models.CharField(max_length=10)
    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['name']

class UncertaintyBand(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255,null=True,blank=True)
    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['name']
          
class Node(models.Model):
    name = models.CharField(max_length=50)
    apsr = models.ForeignKey(AreaOfPotentialSignificantRisk)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now=True)
    
    # geometry
    geometry = models.PointField(srid=2157)
    objects = models.GeoManager()
    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.parent)
    class Meta:
        ordering = ['name']
        
class NodeValue(models.Model):
    scenario = models.ForeignKey(Scenario)
    node = models.ForeignKey(Node)
    elevation = models.FloatField()
    flow = models.FloatField()
    depth = models.FloatField()
    velocity = models.FloatField()
    
    def __unicode__(self):
        return '%s %s' % (self.node, self.scenario)
    class Meta:
        ordering = ['node']

class FloodExtent(models.Model):
    apsr = models.ForeignKey(AreaOfPotentialSignificantRisk)
    apsr_m2m = models.ManyToManyField(AreaOfPotentialSignificantRisk,null=True,blank=True, related_name="apsr_m2m")
    scenario = models.ForeignKey(Scenario)
    status = models.ForeignKey(Status)
    version_type = models.ForeignKey(VersionType)
    availability = models.ForeignKey(Availability)
    # metadata
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now=True)
    # geometry
    geometry = models.MultiPolygonField(srid=2157)
    objects = models.GeoManager()
    
    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s %s' % (self.status, self.scenario)
    #class Meta:
        #ordering = ['apsr']
    
class Uncertainty(models.Model):
    extent = models.ForeignKey(FloodExtent)
    uncertainty_band = models.ForeignKey(UncertaintyBand)
    
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now=True)
    # geometry
    geometry = models.MultiLineStringField(srid=2157)
    objects = models.GeoManager()
    
    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.parent)
    class Meta:
        ordering = ['extent']
        verbose_name_plural = 'flood extent uncertainties'

# predictive flood depth (grid?)

# predictive flood velocity (grid?)

# predictive flood risk (grid?)
