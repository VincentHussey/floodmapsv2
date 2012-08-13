#from django.db import models
from django.contrib.gis.db import models

# Create your models here.

# lookup tables
# class ReportType(models.Model):

# class DataSource(models.Model):

# class FloodCause(models.Model):

# class FloodRecordType(models.Model):

# class FloodSourceType(models.Model):

# class ReportInterpretation(models.Model):

# class FloodInterpretation(models.Model):

# Media
# photographs


# scanned images


# uploaded files


# videos


# reports
class Report(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    #report_type_id = models.ForeignKey(ReportType) # Foreign key
    report_date = models.DateTimeField()
    file_name = models.FielField(upload_to=None,max_length=200)

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
    report = models.ManyToManyField(Report)

    # geometry
    geometry = models.PointField(srid=2147)
    objects = models.GeoManager() 

# other fields in FHM system
    #source_type_id
    #source_river_id
    #source_lake_id
    #source_coastal_water_id
    #source_other
    #number_properties_flodded
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
    #flood_record_type_id

    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)

# historic flood polygons


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




