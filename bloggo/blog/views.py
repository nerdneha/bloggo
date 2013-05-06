# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from bloggo.blog.models import Entry
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse

def front_page(request):
    entries = Entry.objects.all().order_by("-post_date")
    paginator = Paginator(entries,2)

    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        entries = paginator.page(page)
    except (InvalidPage, EmptyPage):
        entries = paginator.page(paginator.num_pages)

    return render_to_response("front.html", dict(entries=entries))



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

