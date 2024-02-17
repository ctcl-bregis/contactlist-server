# ContactList - CTCL 2023-2024
# File: urls.py
# Purpose: App URLs
# Created: January 11, 2024
# Modified: January 11, 2024

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    #path('admin/', admin.site.urls),
    path("", include("main.urls")),
    #path("docs/", include("docs.urls")),
    path('markdownx/', include('markdownx.urls')),
]
