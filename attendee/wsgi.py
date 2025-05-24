import os
import sys

print("=== WSGI DEBUG INFO ===")
print(f"DJANGO_SETTINGS_MODULE: {os.environ.get('DJANGO_SETTINGS_MODULE', 'NOT SET')}")
print(f"Python path: {sys.path}")
print(f"Current working directory: {os.getcwd()}")

# Try to import settings manually
try:
    from django.conf import settings
    print(f"Settings loaded successfully")
    print(f"ROOT_URLCONF: {getattr(settings, 'ROOT_URLCONF', 'NOT FOUND')}")
    print(f"Settings module: {settings.SETTINGS_MODULE}")
except Exception as e:
    print(f"Failed to load settings: {e}")
    import traceback
    traceback.print_exc()

print("=== END WSGI DEBUG INFO ===")

"""
WSGI config for attendee project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

from django.core.wsgi import get_wsgi_application

# Don't override if already set - let environment variable take precedence
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "attendee.settings.development")

application = get_wsgi_application()
