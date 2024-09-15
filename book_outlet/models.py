# book_outlet/models.py

from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify


class Book(models.Model):  # extends the Model class
    title = models.CharField(max_length=50, unique=True)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], default=0
    )
    author = models.CharField(max_length=100, null=True)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)

    def get_absolute_url(self):
        return reverse("book_detail", args=[self.slug])

    def safe(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):  # returns a string representation of the object
        return f"{self.title} ({self.rating})"
