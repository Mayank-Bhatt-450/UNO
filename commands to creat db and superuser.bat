manage.py migrate
manage.py makemigrations
manage.py migrate
manage.py makemigrations
python manage.py syncdb --noinput
echo from django.contrib.auth.models import User; User.objects.create_superuser('bhatt', 'admin@example.com', 'p5kplamps') | python manage.py shell

