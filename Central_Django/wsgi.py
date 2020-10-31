"""
WSGI config for Central_Django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""
# PYTHON IMPORTS
import os
# DJANGO IMPORTS
from django.core.wsgi import get_wsgi_application


os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'Central_Django.settings'
)

application = get_wsgi_application()
