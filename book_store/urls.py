# book_store/urls.py

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("books/", views.books, name="books"),
    path("books/<slug:slug>/", views.book_form, name="book_form"),

    path("authors/", views.authors, name="authors"),
    path("authors/<slug:slug>/", views.author_form, name="author_form"),

    path("countries/", views.countries, name="countries"),
    path("countries/<code>/", views.country_form, name="country_form"),
]
