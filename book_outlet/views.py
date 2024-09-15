from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Book


def index(request):
    return render(request, "book_outlet/index.html", {"books": Book.objects.all()})


def book_detail(request, book_id):
    # Solution 1 - return standard 404 page
    # try:
    #     book = Book.objects.get(id=book_id)
    # except:
    #     raise Http404()
    # Solution 2 - return custom 404 page using built-in shortcut
    book = get_object_or_404(Book, pk=book_id)  # pk is the primary key, same as id
    return render(request, "book_outlet/book_detail.html", {"book": book})


def generic_table_view(request):
    columns = [
        {"name": "title", "title": "Title"},
        {"name": "author", "title": "Author"},
        {"name": "rating", "title": "Rating"},
        {"name": "is_bestselling", "title": "Is best selling ?"},
    ]
    data = Book.objects.all()
    context = {"columns": columns, "data": data}

    return render(request, "book_outlet/generic_table.html", context)
