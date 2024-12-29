# Django Book Store

## Introduction
This is a simple book store application built with Django. 

It was originally created as a project for the Udemy course [Python Django - The Practical Guide](https://www.udemy.com/course/python-django-the-practical-guide/).

I have then used this simple project to test developing generic components (forms and tables) that can be used for multiple models in the application.

The main purpose of this project is to demonstrate how to create an app with multiple pages without requiring to create multiple hmtl files.

## Installation & Usage

- Install [uv](https://docs.astral.sh/uv/), [python](https://www.python.org/downloads/) and [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) on your machine
- `git clone https://github.com/fabrizionastri/book_store` clone the repository to your local machine
- `uv sync` to install the required dependencies and create the virtual environment
- `python manage.py runserver` to start the server

## Admin panel

- `python manage.py createsuperuser` to create a superuser
- `http://http://127.0.0.1:8000/admin` to access the admin panel
