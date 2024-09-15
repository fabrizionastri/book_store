# book_outlet/urls.py

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="all_books"),
    path("<int:book_id>/", views.book_detail, name="book_detail"),
]
