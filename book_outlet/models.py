from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Book(models.Model):  # extends the Model class
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
