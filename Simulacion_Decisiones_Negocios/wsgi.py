"""
WSGI config for Simulacion_Decisiones_Negocios project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "Simulacion_Decisiones_Negocios.settings"
)

application = get_wsgi_application()
