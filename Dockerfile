FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# 👇 PYTHONPATH qo'shing — bu muhim!
ENV PYTHONPATH=/app

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "To_Do_controls.wsgi:application", "--bind", "0.0.0.0:8000"]