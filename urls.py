from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView

from core.views import home, submit, flag

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'slow_loris.views.home', name='home'),
    url(r'^$', home, name='home'),
    url(r'^submit/$', submit, name='submit'),
    url(r'^about$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^flag/(?P<suggestion_id>\d*)/$', flag, name='flag'),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

