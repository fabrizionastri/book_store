# book_outlet/urls.py

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="all_books"),
    path("generic_table/", views.generic_table, name="generic_table"),
    path("<slug:book_slug>/", views.book_detail, name="book_detail"),
]
