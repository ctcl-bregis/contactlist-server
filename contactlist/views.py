# ContactList - CTCL 2023
# Date: June 9, 2023 - June 27, 2023
# Purpose: Main application views

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.template.defaulttags import register
#from django.views.generic import ListView
from datetime import datetime
from . import lib
from .lib import printe
import csv, io

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
    
    context = lib.mkcontext(request, "ContactList - List")
    context["headers"] = columns
    context["data"] = allitems
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
    
    context = lib.mkcontext(request, "ContactList - New")
    context["form"] = form
    return render(request, "new.html", context)


def view(request, inid):
    template = loader.get_template("view.html")
    dbitem = ContactItem.objects.get(pk=inid)
    data = dbitem.todict()
    # Remove database ID
    data.pop("inid")
    headers = lib.getconfig("headers")    
    navbar = lib.navbar()
    
    context = lib.mkcontext(request, "ContactList - View")
    context["headers"] = headers
    context["data"] = data
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
        
        context = lib.mkcontext(request, "ContactList - Edit")
        context["form"] = form
        context["inid"] = inid
        return render(request, "edit.html", context)

def delete(request, inid):
    # The button for continuing with deletion would be a form that does not include data
    if request.method == "POST":
        dbitem = ContactItem.objects.get(inid=inid)
        dbitem.delete()
        return HttpResponseRedirect("/")
    else:
        return render(request, "delconfirm.html", lib.mkcontext(request, "ContactList - Delete Item"))
    
def settings(request):
    if request.method == "POST":
        form = SettingsForm(request.POST)
        if form.is_valid():
            response = HttpResponseRedirect("/")
            response.set_cookie("theme", form.cleaned_data["theme"])
            return response
    else:
        form = SettingsForm()
        
        context = lib.mkcontext(request, "ContactList - Settings")
        context["form"] = SettingsForm()
        return render(request, "settings.html", context)
        
def exportcsv(request):
    allitems = [i.todict() for i in ContactItem.objects.all()]
    fields = ContactItem.fieldnames()
    
    for i in allitems:
        for x in fields:
            # Format any datetime objects as they would be shown on the HTML table
            if isinstance(i[x], datetime):
                i[x] = lib.dt2fmt(i[x])
    
    # Create "file" in memory for DictWriter. This is done to minimize disk writes.
    memcsv = io.StringIO()
    writer = csv.DictWriter(memcsv, fieldnames = fields, delimiter = ",", quoting = csv.QUOTE_ALL)
    writer.writeheader()
    writer.writerows(allitems)
    
    response = HttpResponse()
    response['Content-Disposition'] = "attachment;filename=export.csv"
    response.write(memcsv.getvalue())
    
    return response
    
    
    
    
