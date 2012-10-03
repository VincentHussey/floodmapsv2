from django.contrib.gis.db import models

# Flood relief and Drainage
class LegalInstrument(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255,null=True,blank=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField(null=True,blank=True)
    
    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['name']
        
class Scheme(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255,null=True,blank=True)
    models.ForeignKey(LegalInstrument)
    
    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['name']
        
# Flood defences
# defended areas
class DefendedArea(models.Model):
    scheme = models.ForeignKey(Scheme)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255,null=True,blank=True)
    effective_from = models.DateTimeField()
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now=True)
    
    # geometry
    geometry = models.MultiPolygonField(srid=2157)
    objects = models.GeoManager()
    
    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['scheme','name']

# drainage schemes and flood relief schemes
class SchemeChannel(models.Model):
    scheme = models.ForeignKey(Scheme)
    name = models.CharField(max_length=50)
    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['scheme','name']
        
class SchemeChannelSection(models.Model):
    scheme_channel = models.ForeignKey(SchemeChannel)
    name = models.CharField(max_length=50)
    # geometry
    geometry = models.MultiLineStringField(srid=2157)
    objects = models.GeoManager()
    
    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['scheme_channel','name']
        
class SchemeEmbankment(models.Model):
    scheme = models.ForeignKey(Scheme)
    name = models.CharField(max_length=50)
    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['scheme','name']
        
class SchemeEmbankmentSection(models.Model):
    scheme_embankment = models.ForeignKey(SchemeEmbankment)
    name = models.CharField(max_length=50)
    # geometry
    geometry = models.MultiLineStringField(srid=2157)
    objects = models.GeoManager()
    
    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['scheme_embankment','name']
        
class SchemeBenefitingLand(models.Model):
    scheme = models.ForeignKey(Scheme)
    # geometry
    geometry = models.MultiPolygonField(srid=2157)
    objects = models.GeoManager()
    
    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.scheme)
    class Meta:
        ordering = ['scheme']
        
class SchemeBridge(models.Model):
    scheme_channel = models.ForeignKey(SchemeChannel) # ??? Section
    name = models.CharField(max_length=50)

    # geometry
    geometry = models.PointField(srid=2157)
    objects = models.GeoManager()
    
    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['scheme_channel','name']
        
class SchemeSluice(models.Model):
    scheme_embankment = models.ForeignKey(SchemeEmbankment) # ??? Section
    name = models.CharField(max_length=50)

    # geometry
    geometry = models.PointField(srid=2157)
    objects = models.GeoManager()
    
    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['scheme_embankment','name']
            
class SchemePumpStation(models.Model):
    scheme = models.ForeignKey(Scheme)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255,null=True,blank=True)
    # geometry
    geometry = models.PointField(srid=2157)
    objects = models.GeoManager()
    
    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['scheme','name']

