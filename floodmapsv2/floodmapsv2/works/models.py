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
class Channel(models.Model):
    scheme = models.ForeignKey(Scheme)
    ref = models.CharField(max_length=50)
    name = models.CharField(max_length=50,null=True,blank=True)
    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.ref)
    class Meta:
        ordering = ['scheme','ref']
        
class ChannelSection(models.Model):
    channel = models.ForeignKey(Channel)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255,null=True,blank=True)
    # geometry
    geometry = models.MultiLineStringField(srid=2157)
    objects = models.GeoManager()
    
    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['channel','name']
        
class Embankment(models.Model):
    scheme = models.ForeignKey(Scheme)
    ref = models.CharField(max_length=50)
    name = models.CharField(max_length=50,null=True,blank=True)
    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.ref)
    class Meta:
        ordering = ['scheme','ref']
        
class EmbankmentSection(models.Model):
    embankment = models.ForeignKey(Embankment)
    name = models.CharField(max_length=50)
    # geometry
    geometry = models.MultiLineStringField(srid=2157)
    objects = models.GeoManager()
    
    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['embankment','name']
        
class BenefitingLand(models.Model):
    scheme = models.ForeignKey(Scheme)
    drained = models.BooleanField()
    # geometry
    geometry = models.MultiPolygonField(srid=2157)
    objects = models.GeoManager()
    
    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.scheme)
    class Meta:
        ordering = ['scheme']
        
class Bridge(models.Model):
    channel = models.ForeignKey(Channel) 
    ref = models.CharField(max_length=50)
    name = models.CharField(max_length=50,null=True,blank=True)
    description = models.CharField(max_length=255,null=True,blank=True)
    # geometry
    geometry = models.PointField(srid=2157)
    objects = models.GeoManager()
    
    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['channel','ref']
        
class Sluice(models.Model):
    embankment = models.ForeignKey(Embankment)
    ref = models.CharField(max_length=50)
    name = models.CharField(max_length=50,null=True,blank=True)

    # geometry
    geometry = models.PointField(srid=2157)
    objects = models.GeoManager()
    
    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['embankment','ref']
            
class PumpStation(models.Model):
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

