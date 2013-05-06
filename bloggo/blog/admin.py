from django.contrib import admin
from bloggo.blog.models import Entry

class EntryAdmin(admin.ModelAdmin):
    # fields display on change list
    list_display = ['title']
    # fields to filter the change list with
    list_filter = ['post_date']
    # fields to search in change list
    search_fields = ['title', 'body']
    # enable the date drill down on change list
    date_hierarchy = 'post_date'
    # enable the save buttons on top on change form
    save_on_top = True

admin.site.register(Entry, EntryAdmin)

