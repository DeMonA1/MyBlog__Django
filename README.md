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

        To dump data into file:
        python manage.py dumpdata --indent=2 --output=mysite_data.json (....anage.py --help)

        start docker container of postgresql:
            docker run --name=blog_db -e POSTGRES_DB=blog -e POSTGRES_USER=user -e POSTGRES_PASSWORD=****** -p 5432:5432 -d postgres
        
        and in .env file add:
            DB_NAME, DB_USER, DB_PASSWORD, DB_HOST

        after run this:
        python manage.py migrate

        and after all:
        python loaddata mysite_data.json
        
        If there is a problem appear such as "...DETAIL:  Key (app_label, model)=(blog, post) already exists." just run:

        python manage.py shell

        >>>from django.contrib.contenttypes.models import ContentType
        >>>ContentType.objects.all().delete()

You have to create .env file with:
EMAIL_HOST_USER=<example@gmail.com>
EMAIL_HOST_PASSWORD=from google apppasswords
DEFAULT_FROM_EMAIL=My Blog <example@gmail.com>
