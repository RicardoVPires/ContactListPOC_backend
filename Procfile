web: python manage.py collectstatic --no-input && python manage.py migrate && python manage.py loaddata initial_people && gunicorn contact_list_backend.wsgi --bind 0.0.0.0:$PORT
