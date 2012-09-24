from django.contrib.gis import admin
from floodmaps.models import * 

class MyGeoAdmin(admin.OSMGeoAdmin): # uses WebMercator
	default_lon = -884000 #-8.5 #degrees W
	default_lat = 7061500 # 52.5 #degrees N
	default_zoom = 6
	display_srid = True
	max_width = 800
	max_height = 600
	# map_srid = 900913 # uses WebMercator
	debug = True
	# openlayers_url = 'http://openlayers.org/api/2.12/OpenLayers.js'

admin.site.register(Glossary)
admin.site.register(GlossaryCategory)

# Historic Flood
admin.site.register(ReportType)
admin.site.register(DataSource)
admin.site.register(FloodCause)
admin.site.register(FloodRecordType)
admin.site.register(FloodSourceType)
admin.site.register(QualityCode)
admin.site.register(InterpretationStage)
admin.site.register(ApprovalStatus)
admin.site.register(Report)
admin.site.register(HistoricFlood, MyGeoAdmin) #admin.OSMGeoAdmin)
admin.site.register(ReportInterpretation)
admin.site.register(HistoricFloodInterpretation)
admin.site.register(FloodAddress)
admin.site.register(ReportAddress)
admin.site.register(FloodGroupType)
admin.site.register(FloodGroup)



#admin.site.register()












