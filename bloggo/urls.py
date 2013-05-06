from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # R is a "raw string" this means to treat every character you see as a literal
    # this is mainly used to regular expressions
    # 10 -> is a number literal
    # "hello" -> is a string literal
    # r"hello.*" -> is a raw string literal, used for a regex
    # etc
     url(r'^$', 'bloggo.blog.views.front_page', name='front_page'),
     url(r'^entry$', 'bloggo.blog.views.entry_list', name='entry_list'),
     url(r'^entry/(\d)+$', 'bloggo.blog.views.view_entry', name='view_entry'),
    # url(r'^bloggo/', include('bloggo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
