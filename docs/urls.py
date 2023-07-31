# ContactList - CTCL 2023
# File: urls.py
# Purpose: Integrated Documentation URLs
# Created: July 31, 2023 (copied from CAMS)
# Modified: July 31, 2023

from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path("", views.docs),
    re_path("(?P<path>.*)$", views.docs)
]