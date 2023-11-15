# ContactList - CTCL 2023
# File: urls.py
# Purpose: Main application URLs
# Created: June 9, 2023
# Modified: November 15, 2023

from . import views
from django.urls import include, path
from markdownx import urls as markdownx

urlpatterns = [
    path('markdownx/', include(markdownx)),
    path("", views.index),
    path("new/", views.new),
    path("view/<str:inid>/", views.view),
    path("edit/<str:inid>/", views.edit),
    path("delete/<str:inid>/", views.delete),
    path("settings/", views.settings),
    path("settings/exportcsv/", views.exportcsv),
    path("search/", views.search)
]
