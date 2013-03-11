from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

from slow_loris.core.views import home, submit

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'slow_loris.views.home', name='home'),
    url(r'^$', home, name='home'),
    url(r'^submit/$', submit, name='submit'),
    url(r'^about$', direct_to_template, {'template': 'about.html'}, name='about'),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
