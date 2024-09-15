from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


def index(request):
    return render(request, "book_outlet/index.html", {"books": Book.objects.all()})


def book_detail(request, book_id):
    return render(
        request, "book_outlet/book_detail.html", {"book": Book.objects.get(id=book_id)}
    )
