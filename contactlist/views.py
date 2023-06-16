# ContactList - CTCL 2023
# Date: June 9, 2023 - June 16, 2023
# Purpose: Main application views

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.template.defaulttags import register
from datetime import datetime
import csv
try:
    from .models import ContactItem
except ModuleNotFoundError:
    pass

try:
    from .tableconfig import htmltable
except ModuleNotFoundError:
    pass

try:
    from .fields import ContactForm
except ModuleNotFoundError:
    pass
    
with open("config/database/entry.csv") as f:
    reader = list(csv.DictReader(f))
    
    headers = {i["col"]: i["name"] for i in reader}
    
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
    
def index(request):
    headers = [list(k.keys())[0] for k in htmltable]
    template = loader.get_template("main.html")
    
    allitems = [i.todict() for i in ContactItem.objects.all()]
    
    context = {"title": "ContactList - List", "headers": headers, "headernames": [k[list(k.keys())[0]] for k in htmltable], "data": allitems}
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
    
    return render(request, "new.html", {"title": "ContactList - New", "form": form})

def view(request, inid):
    template = loader.get_template("view.html")
    dbitem = ContactItem.objects.get(pk=inid)
    data = dbitem.todict()
    # Remove database ID
    data.pop("inid")
    
    context = {"title": "ContactList - View", "data": data, "headers": headers}
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
                
        return render(request, "edit.html", {"title": "ContactList - Edit", "form": form, "inid": inid})

def delete(request, inid):
    # TODO: Add confirmation for deleting an item
    dbitem = ContactItem.objects.get(inid=inid)
    dbitem.delete()
    
    return HttpResponseRedirect("/")
