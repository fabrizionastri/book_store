# book_outlet/urls.py

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("books/", views.books, name="books"),
    path("books/<slug:slug>/", views.book_detail, name="book_detail"),
    path("books/<slug:slug>/edit/", views.book_form, name="book_edit"),

    
    path("authors/", views.authors, name="authors"),
    path("authors/<slug:slug>/", views.author_detail, name="author_detail"),
    path("authors/<slug:slug>/edit/", views.author_form, name="author_form"),

    path("countries/", views.countries, name="countries"),
]
