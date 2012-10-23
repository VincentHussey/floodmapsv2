from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView, ListView, DetailView
from predictive.models import *
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(model=UnitOfManagement, template_name="floods_dir_maps.html")),
    url(r'^apsr/(?P<pk>\d+)/$', DetailView.as_view(model=AreaOfPotentialSignificantRisk)),
)

