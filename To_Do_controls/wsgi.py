import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'To_Do_controls.settings')

application = get_wsgi_application()  # <<<<< bu qator muhim!