'''
SET UP A NEW VIRTUAL ENVIRONMENT
python -m venv django_venv 

ACTIVATE VENV
django_venv\scripts\activate.bat

DEACTIVATE VENV
django_venv\scripts\deactivate.bat


CREATE A NEW PROJECT
After installing Django, use 'django-admin startproject name'
to create a project template

START SERVER
Go to the project folder and run 'python manage.py runserver'

DJANGO APPLICATIONS - 
different apps that can be integrated into multiple projects that serve some function

To create a new app - run 'python manage.py startapp first_app'

If you want to add it into your website, you need to add the new app to the 
settings.py of your project


URL Mapping
When the user enters a specific url like 'mysite/home' - Django will detect 'home'
and return a specific response


Templates
Dynamic HTML files - static html + dynamic content using Django Template tags
To use them you need to create a 'templates' folder inside your parent directory.

To be able to run these on different comptuters, you need to get the templates directory
using the Path module inside the project/settings.py file, then add the new variable
to the TEMPLATES/DIR list inside settings.py

example:
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR.joinpath('templates')

To return a template, in views.py you need to return render(request, 'template_name.html', context=ifany)


STATIC FILES
Like Templates, you need to store the STATIC_DIR in a variable and pass it to Django in settings.py
Then you can store all static_dirs as a list under STATIC_URL inside 
STATICFILES_DIRS = [
    STATIC_DIR,
]
You create a folder called static inside the parent project directory where your files will be stored
To load static files in your .html you need to add 
{% load static %} under DOCTYPE in your .html


MODELS
Django models are a built-in feature that
allows Django to create SQL tables, columns, constraints, etc.

To use models you need to access models.py
Each new class is a new SQL table and you can create
variables inside that class that will serve as the columns

Example: 
class WebPage(models.Model):
    topic = models.CharField()
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self) -> str:
        return super().__str__()

To create the SQL model, you need to run
'python manage.py migrate' from inside the parent directory

Then, run 'python manage.py makemigrations app_name'
Then, 'python manage.py migrate'

ADMIN PAGE MODELS
To use your models inside Django's admin page,
go to admins.py within your app folder and add
"from app_name.models import YourModelName, YourModelName2

admin.site.register(YourModelName1)
admin.site.register(YourModelName2)

To use your admin page, it's recommened to add a superuser so only they can use the admin panel
To do this, run "python manage.py createsuperuser" inside the parent directory and
fill in the name, email, and password


Models-Templates-Views Paradigm
1) In views.py import any models that we will need to use
2) Use the view to query the model for data that we'll need
3) Pass results from the model to the template
4) Edit the template so that it is ready to accept and display the data from the model
5) Map a URL to the view
'''
