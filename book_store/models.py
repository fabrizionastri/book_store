# book_store/models.py

from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify


class Country(models.Model):
    class Meta:
        verbose_name_plural = "Countries"

    name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=2, unique=True)

    def get_absolute_url(self):
        return reverse("book_form", args=[self.code])

    @property
    def nr_books(self):
        return self.books.all().count()
    
    def __str__(self):
        return f"{self.name} ({self.code})"
    
    @property
    def slug(self):
        return self.code

class Author(models.Model):
    class Meta:
        verbose_name_plural = "Authors"
        unique_together = ["first_name", "last_name"]

    first_name = models.CharField(max_length=50, null=True, blank=True, db_index=True)
    last_name = models.CharField(max_length=50, null=True, blank=True, db_index=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, null=True, blank=True, db_index=True, related_name="authors")
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def nr_books(self):
        return self.books.all().count()
    
    @property
    def titles(self):
        # return a string with all the books written by the author
        return ", ".join([book.title for book in self.books.all()])

    def get_absolute_url(self):
        return reverse("book_form", args=[self.slug])

    # def save(self, *args, **kwargs):  # not needed if using prepopulated_fields in the admin panel
    #     self.slug = slugify(self)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):  # extends the Model class
    title = models.CharField(max_length=50, unique=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=False, related_name="books")
    is_bestselling = models.BooleanField(default=False)
    published_countries = models.ManyToManyField(Country, related_name="books", blank=True, null=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)

    def get_absolute_url(self):
        return reverse("book_form", args=[self.slug])

    # def save(
    #     self, *args, **kwargs
    # ):  # not needed if using prepopulated_fields in the admin
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    def __str__(self):  # returns a string representation of the object
        return f"{self.title} ({self.rating})"
