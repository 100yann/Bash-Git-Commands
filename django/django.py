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
'''
