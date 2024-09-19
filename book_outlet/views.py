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
    context = {"title": "Books", "columns": columns, "data": data}

    return render(request, "book_outlet/generic_table.html", context)


from django.shortcuts import render, redirect
from .models import Book


def generic_form(request, book_slug=None):

    fields = [
        {"name": "title", "label": "Title"},
        {"name": "author", "label": "Author"},
        {"name": "rating", "label": "Rating"},
        {"name": "is_bestselling", "label": "Is Bestselling"},
    ]

    if request.method == "POST":
        # You can process the submitted form data here
        # Example: handling the submitted form data to save it
        title = request.POST.get("title")
        author = request.POST.get("author")
        rating = request.POST.get("rating")
        is_bestselling = request.POST.get("is_bestselling") == "on"

        # Saving the data to the Book model
        book = Book.objects.create(
            title=title,
            author=author,
            rating=rating,
            is_bestselling=is_bestselling,
        )
        return redirect("all_books")  # Redirect to book listing after saving

    # If GET request, show the form with blank or pre-populated data
    book = get_object_or_404(Book, slug=book_slug)  # pk is the primary key, same as id

    context = {"title": "Add New Book", "fields": fields, "data": book, "mode": "view"}

    return render(request, "book_outlet/generic_form.html", context)
