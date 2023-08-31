set -e

python ./manage.py migrate
export DJANGO_SUPERUSER_PASSWORD=nosecurepassword
python ./manage.py createsuperuser --noinput --username user1 --email user1@mail.com