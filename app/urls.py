# ContactList - CTCL 2023
# Date: June 7, 2023 - June 9, 2023
# Purpose: Meta URLs

from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("contactlist.urls"))
]
