# Django_app

At first, you have to create python virtual environment via:
python3 -m venv my_env

Next,let's activate this:

source my_env/bin/activate
(or deactivate, in depends you demands)

    For creation django project:
    django-admin startproject [name]

    In order to run server:
    python3 manage,py runserver
    
    -//- with a specific host/port:
    python3 manage.py runserver 127.0.0.1:8001 --settings=mysite.settings

    To create app:
    python3 manage.py startapp [blog]

    To access a shell from django app:
    python3 manage.py shell

    TO execute migration:
    python3 manage.py makemigrations [blog]
    
    To create all db migrations:
    python3 manage.py migrate

    To create superuser:
    python3 manage.py createsuperuser
    