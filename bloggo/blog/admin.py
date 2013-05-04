from django.contrib import admin
from blog.models import Entry

class EntryAdmin (admin.ModelAdmin):
    exclude = ['poste_date']

admin.site.register(Entry, EntryAdmin)

