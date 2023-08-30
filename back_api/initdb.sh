set -e

python ./manage.py migrate
export DJANGO_SUPERUSER_PASSWORD=nosecurepassword
python ./manage.py createsuperuser --noinput --username user1 --email user1@mail.com
# python ./manage.py runserver 0.0.0.0:8000