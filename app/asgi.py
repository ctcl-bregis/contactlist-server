# ContactList - CTCL 2023
# File: asgi.py
# Purpose: Django asgi.py config
# Created: June 7, 2023
# Modified: July 31, 2023

"""
ASGI config for contactlist project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

application = get_asgi_application()
