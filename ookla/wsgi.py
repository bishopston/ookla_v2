"""
WSGI config for ookla project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# settings_module = 'ookla.deployment' if 'WEBSITE_HOSTNAME' in os.environ else 'ookla.settings'

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

# application = get_wsgi_application()


# Check for Azure-specific environment variables
is_azure = 'WEBSITE_SITE_NAME' in os.environ and 'WEBSITE_INSTANCE_ID' in os.environ

# Set the Django settings module based on the environment
settings_module = 'ookla.deployment' if is_azure else 'ookla.settings'

os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

# Log the environment variables for debugging (optional)
if is_azure:
    print("Running in Azure Web App environment")
    print(f"WEBSITE_SITE_NAME: {os.environ.get('WEBSITE_SITE_NAME')}")
    print(f"WEBSITE_INSTANCE_ID: {os.environ.get('WEBSITE_INSTANCE_ID')}")
else:
    print("Running in local development environment")

application = get_wsgi_application()