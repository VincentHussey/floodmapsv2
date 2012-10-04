from django.contrib.gis import admin
from floodmaps.admin import MyGeoAdmin
from predictive.models import *

# predictive Floods
admin.site.register(AreaOfSignificantPotentialRisk, MyGeoAdmin) 
admin.site.register(ClimateScenario)
admin.site.register(Status)
admin.site.register(AnnualExceedanceProbabilityScenario) 
admin.site.register(PredictiveSource) 
admin.site.register(PredictiveScenario) 
admin.site.register(PredictiveUncertaintyBand) 
admin.site.register(PredictiveFloodModel) 
admin.site.register(PredictiveFloodNode, MyGeoAdmin) 
admin.site.register(PredictiveFloodExtent, MyGeoAdmin) 
admin.site.register(PredictiveFloodExtentUncertainty, MyGeoAdmin)
