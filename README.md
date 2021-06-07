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
    - virtualenv (optional)

For best use, please use virtualenv instead of global env (OPTIONAL)
1. Make virtualenv `virtualenv <env>`
2. Use env `source <env>/bin/activate` (Linux&Mac) / `<env>/Scripts/activate.bat` (Win)


## Step to Use
1. Clone django starter pack `git clone <git_url>`
2. Go inside folder `cd <cloned_dir>`
3. Install requirements `pip install -r requirements`
4. Create .env file into app/.env `touch app/.env`, then fill in your `DATABASE_NAME`, `DATABASE_USER` & `DATABASE_PASS` (see [docs](https://django-environ.readthedocs.io/en/latest/))
5. Make migration database model (app) `python manage.py makemigrations <app>`
6. Migrate database model `python manage.py migrate`
7. Create superuser `python manage.py createsuperuser --email <email> --username <name>`
8. Run server dev `python manage.py runserver 127.0.0.1:<port>`


### Folder "app" provide django settings
### Folder "main" is sample of django app

Directory tree from root project would be like this:


    .
    ./.gitignore
    ./db.sqlite3
    ./manage.py
    ./README.py
    ./requirements.txt
    ./app
    ./app/__init__.py
    ./app/settings.py
    ./app/urls.py           # main url
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

## Others
Update requirements if needed : `pip freeze > requirements.txt`