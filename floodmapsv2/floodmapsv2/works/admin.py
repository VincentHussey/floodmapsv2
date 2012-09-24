from django.contrib.gis import admin
from floodmaps.admin import MyGeoAdmin
from works.models import *

# defended areas
admin.site.register(DefendedArea)

# schemes
admin.site.register(LegalInstrument)
admin.site.register(Scheme)
admin.site.register(SchemeChannel)
admin.site.register(SchemeChannelSection, MyGeoAdmin)
admin.site.register(SchemeEmbankment)
admin.site.register(SchemeEmbankmentSection, MyGeoAdmin)
admin.site.register(SchemeBenefitingLand, MyGeoAdmin)
admin.site.register(SchemeBridge, MyGeoAdmin)
admin.site.register(SchemeSluice, MyGeoAdmin)
admin.site.register(SchemePumpStation, MyGeoAdmin)
