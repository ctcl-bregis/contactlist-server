# ContactList - CTCL 2023
# File: urls.py
# Purpose: Integrated Documentation URLs
# Created: July 31, 2023
# Modified: November 4, 2023

from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path("", views.docs),
    # Allow any path
    re_path("(?P<path>.*)$", views.docs)
]