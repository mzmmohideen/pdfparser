from django.conf.urls import patterns, include, url
from pdfparserapp.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^pdf_parse_data_feed/',pdf_parse_data_feed),
    # url(r'^$', 'pdfparser.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
