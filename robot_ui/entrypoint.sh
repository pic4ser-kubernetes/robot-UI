python manage.py migrate
python manage.py collectstatic --noinput
gunicorn robot_ui.wsgi --bind 0.0.0.0:8000 --workers=3