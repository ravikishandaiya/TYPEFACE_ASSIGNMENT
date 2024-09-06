#!/bin/sh
# Wait for the database to be available (optional)
echo "Entrypoint file."

# Apply database migrations
echo "Applying migrations..."
python manage.py makemigrations
python manage.py makemigrations apis
python manage.py migrate

# Start the application server
echo "Starting server..."
exec gunicorn dropbox_like_service.wsgi:application --bind 0.0.0.0:8000