from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "rating", "is_bestselling"]
        widgets = {
            "title": forms.TextInput(attrs={"readonly": True}),
            "author": forms.TextInput(attrs={"readonly": True}),
            "rating": forms.NumberInput(attrs={"readonly": True}),
            "is_bestselling": forms.CheckboxInput(attrs={"disabled": True}),
        }
