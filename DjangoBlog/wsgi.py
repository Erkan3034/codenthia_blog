"""
WSGI config for DjangoBlog project.

It exposes the WSGI callable as a module-level variable named ``app``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoBlog.settings')

# Wasmer Edge için 'app' ismi gerekli
app = get_wsgi_application()
application = app  # Geriye uyumluluk için
