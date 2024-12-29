# book_store/admin.py

from django.contrib import admin
from .models import Book, Author, Country


class CountryAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "nr_books")


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "author", "rating", "is_bestselling", "slug")
    list_filter = ("author", "rating", "published_countries")


class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("first_name", "last_name")}
    list_display = ("full_name", "first_name", "last_name", "country", "nr_books", "slug")
    list_filter = ("first_name", "last_name")


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Country, CountryAdmin)
