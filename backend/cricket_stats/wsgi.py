import os  # Add this import statement

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cricket_stats.settings')

application = get_wsgi_application()