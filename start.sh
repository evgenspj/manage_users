python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', password='password')" | python manage.py shell
python manage.py runserver 0.0.0.0:8000
