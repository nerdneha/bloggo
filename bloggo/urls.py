from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

#for future: separate out prefix groups so I don't have 'bloggo.blog.views..." in front of all of the blog views
urlpatterns = patterns('',
     url(r'^$', 'bloggo.blog.views.front_page', name='front_page'),
     url(r'^entry$', 'bloggo.blog.views.entry_list', name='entry_list'),
     url(r'^entry/(\d+)$', 'bloggo.blog.views.view_entry', name='view_entry'),
     url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
     url(r'^logout/$', 'django.contrib.auth.views.logout'),
     url(r'^add/$', 'bloggo.blog.views.add_entry', name='add'),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
