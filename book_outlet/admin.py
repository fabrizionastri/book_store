# book_outlet/admin.py

from django.contrib import admin
from .models import Book, Author, Address, Country


class CountryAdmin(admin.ModelAdmin):

    list_display = ("name", "code", "nr_books")


class AddressAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("street", "country")}
    list_display = (
        "author",
        "street",
        "city",
        "state",
        "postal_code",
        "country",
        "slug",
    )
    list_filter = ("country",)


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "author", "rating", "is_bestselling", "slug")
    list_filter = ("author", "rating", "published_countries")


class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("first_name", "last_name")}
    list_display = ("full_name", "first_name", "last_name", "books_written", "slug")
    list_filter = ("first_name", "last_name")


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Country, CountryAdmin)
