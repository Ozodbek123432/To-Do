#!/bin/bash
echo "Migratsiyalar bajarilmoqda..."
python manage.py migrate --noinput

echo "Static fayllar yig‘ilmoqda..."
python manage.py collectstatic --noinput

echo "Gunicorn ishga tushirilmoqda..."
exec gunicorn To_Do_controls.wsgi:application \
  --bind 0.0.0.0:${PORT:-8000} \
  --workers 2 \
  --timeout 120
