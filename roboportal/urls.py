from django.conf.urls import patterns, include, url
from portal.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'roboportal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', register),
    url(r'^data/$', data),
    url(r'^scoring/$', scoring),
    url(r'^data/$', data),
    url(r'^scoreinitial/$', scoreinitial),
    url(r'^scoreprocess/$', scoreprocess),
    url(r'^printrequest/$', printrequest),
    url(r'^printev/$', printev),
    url(r'^root/$', root),
    url(r'^promote/$', promote),
    url(r'^promote_process/$', promote_process),
    url(r'^login/$', login),
    url(r'^log/$', log),
    url(r'^scorefinal/$', scorefinal),
    url(r'^certi/$', certi),
    url(r'^certiprocess/$', certiprocess),
)
