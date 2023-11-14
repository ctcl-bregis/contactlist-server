# ContactList - CTCL 2023
# File: wsgi.py
# Purpose: WSGI configuration
# Created: June 7, 2023
# Modified: November 4, 2023

"""
WSGI config for contactlist project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'contactlist.settings')

application = get_wsgi_application()
