#!/bin/sh
set -e

if [ -n "$DATABASE_URL" ] && echo "$DATABASE_URL" | grep -Eq "@db:|@postgres:"; then
  echo "Waiting for PostgreSQL..."
  until nc -z db 5432; do
    sleep 1
  done
  echo "PostgreSQL is available"
fi

echo "Applying migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Gunicorn..."
exec gunicorn config.wsgi:application \
  --bind 0.0.0.0:8000 \
  --workers ${GUNICORN_WORKERS:-3} \
  --timeout ${GUNICORN_TIMEOUT:-60}
