# ContactList - CTCL 2023-2024
# File: wsgi.py
# Purpose: WSGI interface
# Created: August 26, 2023
# Modified: August 27, 2023

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

application = get_wsgi_application()
