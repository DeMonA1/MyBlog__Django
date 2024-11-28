# MyBlog

## Main section.

### Launch service. 
To run the Blog app you should:
```
docker compose up
```
If you wanna run it without a container (in local environment),
first of all, you should run the PostgresQL image as it'll be
described below.

### Migration db to PostgreSQL
To dump data into file:
```
python manage.py dumpdata --indent=2 --output=mysite_data.json (for help: mananage.py --help)
```
Launch the PostgresQL docker container:
> [!CAUTION]
> take it from .env file
```
    docker run --name=blog_db -e POSTGRES_DB=blog -e POSTGRES_USER=user -e POSTGRES_PASSWORD=****** -p 5432:5432 -d postgres
```
and in .env file add:
    DB_NAME, DB_USER, DB_PASSWORD, DB_HOST

After, apply migrations via:
```
python manage.py migrate
```

Finally, load data from json file as follows:
```
python loaddata mysite_data.json
```
> [!TIP]
> If there is a problem appear such as "...DETAIL:  Key (app_label, model)=(blog, post) already exists." just run:
> ```
> python manage.py shell
> ```
> In the shell, run follows:
> ```
> from django.contrib.contenttypes.models import ContentType
> ContentType.objects.all().delete()
> ```
### PostgreSQL extensions
In order to add postgresql extension, for example, like triagram, you have to:
```
python manage.py makemigrations --name=trigram_ext --empty blog
```
Next, edit the migrations file adding into it operations field:
    TriagramExtension()

### :dart: Settings
To send share-letter not using email, use 
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' into settings.
    
You have to create .env file with:  
EMAIL_HOST_USER=<example@gmail.com>
EMAIL_HOST_PASSWORD=from google apppasswords
DEFAULT_FROM_EMAIL=My Blog <example@gmail.com>

## _Basic Django commands_

At first, you have to create python virtual environment via:
```
python3 -m venv my_env
```
Next,let's activate this<sub>(or deactivate, in depends you demands)</sub>:
```
source my_env/bin/activate
```
For creation django project:
```
django-admin startproject [name]
```
In order to run server:
```
python3 manage.py runserver
```
-//- with a specific host/port and settings:
```
python3 manage.py runserver 127.0.0.1:8001 --settings=mysite.settings
```
To create app:
```
python3 manage.py startapp [blog]
```
To access a shell from django app:
```
python3 manage.py shell
```
TO execute migration:
```
python3 manage.py makemigrations [blog]
```
To create all db migrations:
```
python3 manage.py migrate
```
To create superuser:
```
python3 manage.py createsuperuser
```

Link to basic commands: [Link Text](#basic-django-commands)
