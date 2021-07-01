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

Generate Openapi (i.e. swagger html in `<app>/templates/swagger-ui.html`):
python manage.py generateschema --file `<app>/static/openapi-schema.yml`


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
5. Fill in your env in app/.env (see [docs](https://django-environ.readthedocs.io/en/latest/#installation))
- `SECRET_KEY` (Github ENV)
- `DEBUG` (True)
- `DATABASE_NAME`
- `DATABASE_USER`
- `DATABASE_PASS`
- `REDIS_KEY`
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
    ./product
    ./product/migrations       # Migration app
    ./product/static           # Static dir app
    ./product/templates        # Template view app
    ./product/__init__.py
    ./product/admin.py         # admin controller
    ./product/api.py           # api controller
    ./product/apps.py
    ./product/forms.py         # model form app
    ./product/metadata.py      # metadata api controller
    ./product/models.py        # model app
    ./product/serializers.py   # serializer api controller
    ./product/tests.py
    ./product/urls.py          # url app
    ./product/views.py         # view controller

#### NOTE:

- Folder "app" provide django settings
- Folder "product" is sample of django app
- For sample endpoint `127.0.0.1:<port>/product/<id>`, redis should be activated
- For Django Rest Framework, best practice is using Generic API View (i.e. in "product" app), see [details](https://www.django-rest-framework.org/api-guide/generic-views/) and [example1](https://medium.com/analytics-vidhya/django-rest-framework-views-generic-views-viewsets-simplified-ff997ea3205f) or [example2](https://juliensalinas.com/en/django-rest-framework-generic-views/)
- Demo customizing Django default User has been modified from "account" app, see [details](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project)
- Demo token authentication Django default has been implemented from `urls.py` in "account" app, see [details](https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication)

## Others
Update requirements if needed : `pip freeze > requirements.txt`

Using swagger ui : this [link](https://www.django-rest-framework.org/api-guide/schemas/)

Using Redis cache in Django: this [link](https://realpython.com/caching-in-django-with-redis/)

Using Memcached cache in Django: this [link](https://docs.djangoproject.com/en/3.2/topics/cache/)

Using 2FA / MFA in Django : using pyotp, see this [link](https://github.com/pyauth/pyotp) and [example](https://www.section.io/engineering-education/implementing-totp-2fa-using-flask/)
