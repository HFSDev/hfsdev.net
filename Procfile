release: python manage.py migrate
web: gunicorn --timeout 360 hfsdev_backend.wsgi --log-file -
