# ContactList - CTCL 2023-2024
# File: asgi.py
# Purpose: ASGI interface
# Created: January 11, 2024
# Modified: January 11, 2024

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

application = get_asgi_application()
