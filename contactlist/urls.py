# ContactList - CTCL 2023
# Date: June 9, 2023 - June 13, 2023
# Purpose: Main application URLs

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("new/", views.new),
    path("item/<str:inid>", views.item)
]
