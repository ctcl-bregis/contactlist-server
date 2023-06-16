# ContactList - CTCL 2023
# Date: June 9, 2023 - June 13, 2023
# Purpose: Main application views

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.template.defaulttags import register
from datetime import datetime
import csv
try:
    from .models import ContactItem
    from .tableconfig import htmltable
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
            setattr(newentry, "crd", dt)
            setattr(newentry, "mod", dt)
            
            newentry.save()
            
            return HttpResponseRedirect("/")
    else:
        form = ContactForm
    
    return render(request, "new.html", {"form": form})

def item(request, inid):
    action = request.GET.get("action", "")
    
    if action == "edit":
        return HttpResponse("Not implemented")
    elif action == "delete" or action == "del":
        # TODO: Add confirmation for deleting an item
        dbitem = ContactItem.objects.get(inid=inid)
        dbitem.delete()
        
        return HttpResponseRedirect("/")
    # If an invalid "action" is specified or there is no parameter, just default to "view"
    else:
        template = loader.get_template("view.html")
        dbitem = ContactItem.objects.get(pk=inid)
        data = dbitem.todict()
        # Remove database ID
        data.pop("inid")
        
        context = {"data": data, "headers": headers}
        return HttpResponse(template.render(context, request))
    

    
