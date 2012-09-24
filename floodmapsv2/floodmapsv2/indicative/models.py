from django.contrib.gis.db import models

# Create your models here.
## Indicative Floods
# indicative flood polygons
class IndicativeFloodDataset(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255,null=True,blank=True)
    abstract = models.TextField(null=True,blank=True)
    metadata = models.URLField(null=True,blank=True)
    # release_version

    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['name']

class IndicativeFloodCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255,null=True,blank=True)
    
    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'indicative flood categories'
        
class IndicativeFlood(models.Model):
    dataset = models.ForeignKey(IndicativeFloodDataset)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50)
    category = models.ForeignKey(IndicativeFloodCategory)
    # geometry
    geometry = models.MultiPolygonField(srid=2157)
    objects = models.GeoManager()
    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['name']
