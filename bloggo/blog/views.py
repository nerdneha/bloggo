# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

from models import Entry

def hello_world(request):
    return HttpResponse("Hello world!")

def froogle(request):
    return HttpResponse("Blah!")

def entry_list(request):
    entries = Entry.objects.all()
    return render(request, "entry_list.html", {"entries": entries})

def entry_detail(request, entry_id):
    try:
        entry = Entry.objects.get(pk=entry_id)
    except Entry.DoesNotExist:
        return HttpResponse (status=404)
    return render(request, "entry_detail.html", {"entry": entry})

# creates a link to blog post number 51 on handler named entry_detail
# reverse("entry_detail", 51)
# "http://mysite.com/entry/51"

