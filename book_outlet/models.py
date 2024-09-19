# book_outlet/models.py

from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify


class Country(models.Model):
    name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=2, unique=True)

    def nr_books(self):
        return self.books.all().count()

    def __str__(self):
        return f"{self.name} ({self.code})"

    def get_absolute_url(self):
        return reverse("country_detail", args=[self.code])

    class Meta:
        verbose_name_plural = "Countries"


class Address(models.Model):
    street = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    postal_code = models.CharField(max_length=6, null=True)
    country = models.CharField(max_length=50, null=True)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.postal_code}, {self.country}"

    def get_absolute_url(self):
        return reverse("address_detail", args=[self.slug])

    # def save(
    #     self, *args, **kwargs
    # ):  # not needed if using prepopulated_fields in the admin
    #     self.slug = slugify(self)
    #     super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Addresses"


class Author(models.Model):
    first_name = models.CharField(max_length=50, unique=True)
    last_name = models.CharField(max_length=50, unique=True)
    address = models.OneToOneField(
        Address,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    slug = models.SlugField(default="", blank=True, null=False, db_index=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # returns the number of books written by the author
    def books_written(self):
        return self.books.all().count()

    def get_absolute_url(self):
        return reverse("author_detail", args=[self.slug])

    # def save(
    #     self, *args, **kwargs
    # ):  # not needed if using prepopulated_fields in the admin
    #     self.slug = slugify(self)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):  # extends the Model class
    title = models.CharField(max_length=50, unique=True)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], default=0
    )
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name="books"
    )
    is_bestselling = models.BooleanField(default=False)
    published_countries = models.ManyToManyField(
        Country, related_name="books", blank=True
    )
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)

    def get_absolute_url(self):
        return reverse("book_detail", args=[self.slug])

    # def save(
    #     self, *args, **kwargs
    # ):  # not needed if using prepopulated_fields in the admin
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    def __str__(self):  # returns a string representation of the object
        return f"{self.title} ({self.rating})"
