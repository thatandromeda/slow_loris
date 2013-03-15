import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "slow_loris.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()