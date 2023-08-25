python manage.py migrate &
python manage.py collectstatic --noinput &
python manage.py runserver 0.0.0.0:8000
# gunicorn robot_ui.wsgi --bind 0.0.0.0:8000 --workers=3