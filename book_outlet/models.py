from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Book(models.Model):  # extends the Model class
    title = models.CharField(max_length=50, unique=True)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], default=0
    )
    author = models.CharField(max_length=100, null=True)
    is_bestselling = models.BooleanField(default=False)

    def __str__(self):  # returns a string representation of the object
        return f"{self.title} ({self.rating})"
