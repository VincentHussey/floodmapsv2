#from django.db import models
from django.contrib.gis.db import models

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^django\.contrib\.gis"])

# glossary
class GlossaryCategory(models.Model):
   name = models.CharField(max_length=50)

   # Returns the string representation of the model.
   def __unicode__(self):
       return '%s' % (self.name)
   class Meta:
       ordering = ['name']
       verbose_name_plural = 'glossary categories'

class Glossary(models.Model):
    category = models.ForeignKey(GlossaryCategory)
    term = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)

    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.term)
    class Meta:
        ordering = ['category','term']
        verbose_name_plural = 'glossary entries'

# lookup tables
class ReportType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100,null=True,blank=True)
    initial = models.CharField(max_length=2)
    default_extension = models.CharField(max_length=4,null=True,blank=True)
    default_folder = models.CharField(max_length=100,null=True,blank=True)
    #default_extent 
    #default_level
    #default_depth
    #default_velocity
    #default_flow
    #default_frequency
    #default_financialdamage
    #default_source
    #default_cause
    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['name']

class DataSource(models.Model):
   name = models.CharField(max_length=50)
   description = models.CharField(max_length=50,null=True,blank=True)
   initial = models.CharField(max_length=5)
   default_folder = models.CharField(max_length=100)

   # Returns the string representation of the model.
   def __unicode__(self):
       return '%s' % (self.name) 
   class Meta:
       ordering = ['name']

class FloodCause(models.Model):
   name = models.CharField(max_length=50)
   description = models.CharField(max_length=100,null=True,blank=True)

   # Returns the string representation of the model.
   def __unicode__(self):
       return '%s' % (self.name)
   class Meta:
       ordering = ['name']

class FloodRecordType(models.Model):
   name = models.CharField(max_length=50)
   description = models.CharField(max_length=100,null=True,blank=True)

   # Returns the string representation of the model.
   def __unicode__(self):
       return '%s' % (self.name)
   class Meta:
       ordering = ['name']

class FloodSourceType(models.Model):
   name = models.CharField(max_length=50)
   description = models.CharField(max_length=100,null=True,blank=True)

   # Returns the string representation of the model.
   def __unicode__(self):
       return '%s' % (self.name)
   class Meta:
       ordering = ['name']

class QualityCode(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=40,null=True,blank=True)

    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['name']

class InterpretationStage(models.Model):
    name = models.CharField(max_length=40)

    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['name']

class ApprovalStatus(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200,null=True,blank=True)

    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'approval status'

class FloodRecordType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200,null=True,blank=True)

    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['name']
    

# Media
# photographs


# scanned images



# videos


# reports
class Report(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    report_type = models.ForeignKey(ReportType,null=True) # Foreign key
    report_date = models.DateTimeField()
    file_name = models.FileField(upload_to='report/%Y/%m/%d/',max_length=200)

    # other fields from FHM system

    #directory_location
    #report_source_id
    #entered_by_id
    #entered_date
    #available_on_web
    #owner_id
    #owner_department
    #local_archive_refid
    #information_source
    #scan_status_id
    #department_id
    #defence_asset_info
    #predictive_map_info

    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)

# Historic Floods
# historic flood points
class HistoricFlood(models.Model):
    name = models.CharField(max_length=100)
    start = models.DateTimeField()
    end = models.DateTimeField()
    notes = models.TextField()

    # link to report from floods - floods fields have been split by geometry and type.
    report = models.ManyToManyField(Report) # through field?

    cause = models.ManyToManyField(FloodCause, through='FloodCauseLink')
    #address = models.ForeignKey(FloodAddress) # needs a bit of though on implementation ?
    group = models.ManyToManyField('FloodGroup', null=True, blank=True)
    flood_record_type = models.ForeignKey(FloodRecordType,null=True)

    # geometry
    geometry = models.PointField(srid=2147)
    objects = models.GeoManager() 

# other fields in FHM system
    #source_type_id
    #source_river_id
    #source_lake_id
    #source_coastal_water_id
    #source_other
    #number_properties_flooded
    #financial_damage
    #catchment_id
    #peak_date_time
    #peak_level
    #peak_depth
    #peak_velocity
    #frequency
    #alleviation_scheme
    #peak_flow
    #scheme_description
    #severity_index
    #geographical_quality_id
    #tmp_ftr_typ

    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['name']

# historic flood polygons


class ReportInterpretation(models.Model):
    report = models.ForeignKey(Report)
    quality_code = models.ForeignKey(QualityCode)
    interpretation_stage = models.ForeignKey(InterpretationStage)
    stage_date = models.DateTimeField()
    #first_person
    justification = models.CharField(max_length=200) 

    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['report']


class HistoricFloodInterpretation(models.Model):
    flood = models.ForeignKey(HistoricFlood)    
    quality_code = models.ForeignKey(QualityCode)
    #interpretation_stage    
    stage_date = models.DateTimeField()
    #first_person
    justification = models.CharField(max_length=200)
    #approver
    
    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.flood)
    class Meta:
        ordering = ['flood']

class FloodAddress(models.Model):
    flood = models.ForeignKey(HistoricFlood)
    report = models.ForeignKey(Report,null=True,blank=True)
    #townland
    #town
    #county
    #name
    #building_number
    #street
    class Meta:
        ordering = ['flood']
        verbose_name_plural = 'flood addresses'

class ReportAddress(models.Model):
    report = models.ForeignKey(Report)
    #townland
    #town
    #county
    #name
    #building_number
    #street
    class Meta:
        ordering = ['report']
        verbose_name_plural = 'report addresses'

class FloodCauseLink(models.Model):
    flood = models.ForeignKey(HistoricFlood)
    cause = models.ForeignKey(FloodCause)
    report = models.ForeignKey(Report,null=True,blank=True)

    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.cause)

class FloodReportLink(models.Model):
    flood = models.ForeignKey(HistoricFlood)
    report = models.ForeignKey(Report,null=True,blank=True)
    #extent
    #level
    #depth
    #velocity
    #flow
    #frequency
    #number_properties_damaged
    #financial_damage_caused
    #source
    #cause
    #entered_by
    #completed

class FloodGroupType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255,null=True,blank=True)

    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['name']

class FloodGroup(models.Model):
    type = models.ForeignKey(FloodGroupType)
    description = models.CharField(max_length=255,null=True,blank=True)

    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)
    class Meta:
        ordering = ['type']

# Indicative Floods
# indicative flood polygons



# Predictive Floods
# predictive flood polygons




# predictive flood risk (grid?)



# predictive flood depth (grid?)



# predictive flood velocity (grid?)



# Flood defences
# defended areas



# drainage schemes and flood relief schemes




