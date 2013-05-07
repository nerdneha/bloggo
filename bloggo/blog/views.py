# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from bloggo.blog.models import Entry
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from bloggo.blog.forms import AddPostForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

def front_page(request):
    entries = Entry.objects.all().order_by("-post_date")
    paginator = Paginator(entries,5)

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

def add_entry(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            title = cd['title']
            body = cd['body']
            entry_obj = Entry(title=title, body=body)
            entry_obj.save()
            return HttpResponseRedirect("/")
    else:
        form = AddPostForm()
    return render(request, 'add_entry.html', locals())
