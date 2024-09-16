from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Book
from django.db.models import Avg, Min, Max


def index(request):
    books = Book.objects.all().order_by("title")

    return render(
        request,
        "book_outlet/index.html",
        {
            "books": books,
            "number_of_books": books.count(),
            "stats": books.aggregate(
                avg=Avg("rating"), min=Min("rating"), max=Max("rating")
            ),
        },
    )


def book_detail(request, book_slug):
    # Solution 1 - return standard 404 page
    # try:
    #     book = Book.objects.get(id=book_id)
    # except:
    #     raise Http404()
    # Solution 2 - return custom 404 page using built-in shortcut
    # book = get_object_or_404(Book, pk=book_id)  # pk is the primary key, same as id
    book = get_object_or_404(Book, slug=book_slug)  # pk is the primary key, same as id
    return render(request, "book_outlet/book_detail.html", {"book": book})


def generic_table(request):
    columns = [
        {"name": "title", "title": "Title"},
        {"name": "author", "title": "Author"},
        {"name": "rating", "title": "Rating"},
        {"name": "is_bestselling", "title": "Is best selling ?"},
    ]
    data = Book.objects.all()
    context = {"columns": columns, "data": data}

    return render(request, "book_outlet/generic_table.html", context)
