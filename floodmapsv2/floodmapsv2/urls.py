from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
from django.contrib.gis import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name="home.html")),
    url(r'^frm$', TemplateView.as_view(template_name="frm-home.html")),
    url(r'^map$', TemplateView.as_view(template_name="map.html")),
    url(r'^test-map$', TemplateView.as_view(template_name="test-map.html")),
    url(r'^predictive/', include('predictive.urls')),

    # urls for apps
    #url(r'^$',include('floodmapsv2.floodmaps.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
