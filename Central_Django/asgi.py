"""
ASGI config for Central_Django project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""
# PYTHON IMPORTS
import os
# DJANGO IMPORTS
from django.core.asgi import get_asgi_application


os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'Central_Django.settings'
)

application = get_asgi_application()
