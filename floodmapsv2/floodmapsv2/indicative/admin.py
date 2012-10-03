from django.contrib.gis import admin
from floodmaps.admin import MyGeoAdmin
from indicative.models import *

# Indicative Flood
admin.site.register(IndicativeFloodDataset)
admin.site.register(IndicativeFloodCategory)
admin.site.register(IndicativeFlood, MyGeoAdmin)


