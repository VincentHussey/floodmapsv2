from django.contrib.gis import admin
from floodmaps.admin import MyGeoAdmin
from predictive.models import *

# Inlines
class NodeValueInline(admin.TabularInline):
    model = NodeValue
    
class NodeAdmin(MyGeoAdmin):
    inlines = [NodeValue]


# predictive Floods
admin.site.register(Status)
admin.site.register(VersionType)
admin.site.register(Availability)
admin.site.register(UnitOfManagement)
admin.site.register(AreaOfPotentialSignificantRisk, MyGeoAdmin)
admin.site.register(Climate)
admin.site.register(AnnualExceedanceProbability) 
admin.site.register(Source) 
admin.site.register(Scenario) 
admin.site.register(UncertaintyBand) 
admin.site.register(Node, MyGeoAdmin) 
admin.site.register(NodeValue)
admin.site.register(FloodExtent, MyGeoAdmin) 
admin.site.register(Uncertainty, MyGeoAdmin)
