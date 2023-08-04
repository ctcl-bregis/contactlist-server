# ContactList - CTCL 2023
# File: urls.py
# Purpose: App URLs
# Created: June 6, 2023
# Modified: August 3, 2023

from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("martor/", include("martor.urls")),
    path("", include("contactlist.urls")),
    path("docs/", include("docs.urls"))
]
