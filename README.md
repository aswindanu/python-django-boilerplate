## Basic Django Command
Create new django: 
django-admin startproject `<name>`

Create new app: 
python manage.py startapp `<app>`

Migration :
python manage.py makemigrations `<app>`
python manage.py migrate

Create superuser :
python manage.py createsuperuser --email `<email>` --username `<name>`

Serve dev:
python manage.py runserver `<ip>`:`<port>`


## Prequisition
What need to be installed
    
    - pip
    - python
    - django
    - redis (optional)
    - virtualenv (optional)


For best use, please use cache redis (OPTIONAL)
1. Download and activate redis, [link](https://riptutorial.com/redis/example/29962/installing-and-running-redis-server-on-windows) (Windows)

For best use, please use virtualenv instead of global env (OPTIONAL)
1. Make virtualenv `virtualenv <env>`
2. Use env `source <env>/bin/activate` (Linux&Mac) / `<env>/Scripts/activate.bat` (Windows)


## Step to Use
1. Clone django starter pack `git clone <git_url>`
2. Go inside folder `cd <cloned_dir>`
3. Install requirements `pip install -r requirements`
4. Create .env file into app/.env `touch app/.env`
5. Fill in your `DATABASE_NAME`, `DATABASE_USER`, `DATABASE_PASS`, `REDIS_KEY` in app/.env (see [docs](https://django-environ.readthedocs.io/en/latest/#installation))
6. Make migration database model (app) `python manage.py makemigrations <app>`
7. Migrate database model `python manage.py migrate`
8. Create superuser `python manage.py createsuperuser --email <email> --username <name>`
9. Run server dev `python manage.py runserver 127.0.0.1:<port>`
10. Open from browser `127.0.0.1:<port>`

Directory tree from root project would be like this:


    .
    ./.gitignore
    ./db.sqlite3
    ./manage.py
    ./README.py
    ./requirements.txt
    ./app
    ./app/__init__.py
    ./app/settings.py       # setting project
    ./app/urls.py           # main url project
    ./app/wsgi.py
    ./main
    ./main/migrations       # Migration app
    ./main/static           # Static dir app
    ./main/templates        # Template view app
    ./main/__init__.py
    ./main/admin.py         # admin controller
    ./main/api.py           # api controller
    ./main/apps.py
    ./main/forms.py         # model form app
    ./main/models.py        # model app
    ./main/serializers.py   # serializer api controller
    ./main/tests.py
    ./main/urls.py          # url app
    ./main/views.py         # view controller

#### NOTE:

- Folder "app" provide django settings
- Folder "main" is sample of django app
- For sample endpoint `127.0.0.1:<port>/product/<id>`, redis should be activated

## Others
Update requirements if needed : `pip freeze > requirements.txt`

Using Redis cache in Django: this [link](https://realpython.com/caching-in-django-with-redis/)

Using Memcached cache in Django: this [link](https://docs.djangoproject.com/en/3.2/topics/cache/)
