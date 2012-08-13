from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView, DetailView
from floodmapsv2.floodmaps.models import *
from floodmapsv2.floodmaps.views import SensorListView

urlpatterns = patterns('',
    #url(r'^$', 'floodmapsv2.floodmaps.views.create_map'),
)

