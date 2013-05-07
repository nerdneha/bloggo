# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from bloggo.blog.models import Entry
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login

def front_page(request):
    entries = Entry.objects.all().order_by("-post_date")
    paginator = Paginator(entries,2)

    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        entries = paginator.page(page)
    except (InvalidPage, EmptyPage):
        entries = paginator.page(paginator.num_pages)

    return render_to_response("front.html", locals())

def entry_list(request):
    entries = Entry.objects.all()
    return render(request, "entry_list.html", locals())

def view_entry(request, entry_id):
    entry = get_object_or_404(Entry,pk=entry_id)
    return render(request, "entry_detail.html", locals())

