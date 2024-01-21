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

application = get_wsgi_application()