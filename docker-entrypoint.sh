#!/bin/bash

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python3 manage.py makemigrations
python manage.py migrate

# Start server
echo "Starting server"
