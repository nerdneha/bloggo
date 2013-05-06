from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
     url(r'^$', 'bloggo.blog.views.front_page', name='front_page'),
     url(r'^entry$', 'bloggo.blog.views.entry_list', name='entry_list'),
     url(r'^entry/(\d)+$', 'bloggo.blog.views.view_entry', name='view_entry'),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
