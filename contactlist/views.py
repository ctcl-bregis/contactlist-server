# ContactList - CTCL 2023
# Date: June 9, 2023 - June 23, 2023
# Purpose: Main application views

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.template.defaulttags import register
from datetime import datetime
from . import lib
from . import __version__
from .lib import printe
import csv

try:
    from .models import ContactItem
except ModuleNotFoundError:
    pass

try:
    from .fields import ContactForm, SettingsForm
except ModuleNotFoundError:
    pass

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
    
def index(request):
    template = loader.get_template("main.html")
    headers = lib.getconfig("headers")
    
    # htmltable in the config should not contain titles, so add them from headers
    columns = []
    for i in lib.getconfig("htmltable"):
        if i["type"] == "info":
            i["title"] = headers[i["col"]]
        elif i["type"] == "button":
            i["title"] = ""
            
        columns.append(i)
    
    allitems = [i.todict() for i in ContactItem.objects.all()]
    
    tmplst = []
    for i in allitems:
        i["tcrd"] = lib.dt2fmt(i["tcrd"])
        i["tmod"] = lib.dt2fmt(i["tmod"])
        tmplst.append(i)
    allitems = tmplst
    
    navbar = lib.navbar()
    context = {"title": "ContactList - List", "headers": columns, "data": allitems, "styling": lib.theme(request.COOKIES.get("theme"))["styling"], "navbar": navbar, "ver": __version__}
    return HttpResponse(template.render(context, request))

def new(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            newentry = ContactItem()
            cld = form.cleaned_data
            for k, v in cld.items():
                setattr(newentry, k, v)
            
            dt = datetime.now()
            setattr(newentry, "tcrd", dt)
            setattr(newentry, "tmod", dt)
            
            newentry.save()
            
            return HttpResponseRedirect("/")
    else:
        form = ContactForm
    
    return render(request, "new.html", {"title": "ContactList - New", "form": form, "styling": lib.theme(request.COOKIES.get("theme"))["styling"], "navbar": lib.navbar(), "ver": __version__})

def view(request, inid):
    template = loader.get_template("view.html")
    dbitem = ContactItem.objects.get(pk=inid)
    data = dbitem.todict()
    # Remove database ID
    data.pop("inid")
    
    headers = lib.getconfig("headers")
    
    navbar = lib.navbar()

    context = {"title": "ContactList - View", "data": data, "headers": headers, "styling": lib.theme(request.COOKIES.get("theme"))["styling"], "navbar": navbar, "ver": __version__}
    return HttpResponse(template.render(context, request))

def edit(request, inid):
    if request.method == "POST":
        data = ContactItem.objects.get(pk=inid)
        form = ContactForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            
            data = ContactItem.objects.get(pk=inid)
            data.tmod = datetime.now()
            data.save()
            
            return HttpResponseRedirect("/")
    else:
        data = ContactItem.objects.get(pk=inid)
        form = ContactForm(initial = data.todict())
                
        return render(request, "edit.html", {"title": "ContactList - Edit", "form": form, "inid": inid, "styling": lib.theme(request.COOKIES.get("theme"))["styling"], "navbar": lib.navbar, "ver": __version__})

def delete(request, inid):
    # TODO: Add confirmation for deleting an item
    dbitem = ContactItem.objects.get(inid=inid)
    dbitem.delete()
    
    return HttpResponseRedirect("/")
    
def settings(request):
    if request.method == "POST":
        form = SettingsForm(request.POST)
        if form.is_valid():
            
            response = HttpResponseRedirect("/")
            response.set_cookie("theme", form.cleaned_data["theme"])
            return response
    else:
        form = SettingsForm()
        
        return render(request, "settings.html", {"title": "ContactList - Settings", "form": form, "styling": lib.theme(request.COOKIES.get("theme"))["styling"], "navbar": lib.navbar, "ver": __version__})
            
    
