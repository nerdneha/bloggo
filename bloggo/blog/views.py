# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from bloggo.blog.models import Entry


def hello_world(request):
    return HttpResponse("Hello world!")

def recent_list(request):
    recent_entries = Entry.objects.all()[:5]
    return render(request, "recent_list.html", locals())


def entry_list(request):
    entries = Entry.objects.all()
    return render(request, "entry_list.html", locals())

def view_entry(request, entry_id):
    print "we got here"
    entry = get_object_or_404(Entry,pk=entry_id)
    return render(request, "entry_detail.html", locals())
'''
def add_entry(request):
    return render(request, "
'''
# creates a link to blog post number 51 on handler named entry_detail
# reverse("entry_detail", 51)
# "http://mysite.com/entry/51"

