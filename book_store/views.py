from .models import Author, Book, Country
from django.db.models import Avg, Min, Max
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect


def index(request):
    books = Book.objects.all().order_by("title")

    return render(
        request,
        "book_store/index.html",
        {
            "books": books,
            "number_of_books": books.count(),
            "stats": books.aggregate(
                avg=Avg("rating"), min=Min("rating"), max=Max("rating")
            ),
        },
    )


def books(request):
    columns = [
        {"name": "title", "title": "Title"},
        {"name": "author", "title": "Author"},
        {"name": "rating", "title": "Rating"},
        {"name": "is_bestselling", "title": "Is best selling ?"},
        {"name": "slug", "title": "Slug"},
    ]
    data = Book.objects.all()
    context = {"title": "Books", "columns": columns, "data": data}

    return render(request, "book_store/generic_table.html", context)


def book_detail(request, slug):
    # Solution 1 - return standard 404 page
    # try:
    #     book = Book.objects.get(id=book_id)
    # except:
    #     raise Http404()
    # Solution 2 - return custom 404 page using built-in shortcut
    # book = get_object_or_404(Book, pk=book_id)  # pk is the primary key, same as id
    book = get_object_or_404(Book, slug=slug)  # pk is the primary key, same as id
    return render(request, "book_store/book_detail.html", {"book": book})



def countries(request):
    columns = [
        {"name": "name", "title": "Name"},
        {"name": "code", "title": "Code"},
        {"name": "nr_books", "title": "Number of Books"},
    ]
    data = Country.objects.all().order_by("name")
    context = {"title": "Books", "columns": columns, "data": data}

    return render(request, "book_store/generic_table.html", context)


def authors(request):
    columns = [
        {"name": "full_name", "title": "Name"},
        {"name": "nr_books", "title": "Number of Books"},
        {"name": "titles", "title": "Titles"},
        {"name": "slug", "title": "Slug"},
    ]
    data = Author.objects.all().order_by("first_name")
    context = {"title": "Authors", "columns": columns, "data": data}

    return render(request, "book_store/generic_table.html", context)

def book_form(request, slug=None):
    if request.method == "POST":
        book = Book.objects.create(
            title=request.POST.get("title"),
            author=request.POST.get("author"),
            rating=request.POST.get("rating"),
            is_bestselling=request.POST.get("is_bestselling") == "on",
            slug=request.POST.get("slug"),
        )
        print("Book created:", book)
        return redirect("index")  # Redirect to book listing after saving

    # If GET request, render the form with the data
    fields = [
        {"name": "title", "label": "Title"},
        {"name": "author", "label": "Author"},
        {"name": "rating", "label": "Rating"},
        {"name": "is_bestselling", "label": "Is Bestselling"},
        {"name": "slug", "label": "Slug"},
    ]
    data = get_object_or_404(Book, slug=slug)  # pk is the primary key, same as id

    context = {"title": "Add new book", "fields": fields, "data": data, "mode": "view"}

    return render(request, "book_store/generic_form.html", context)


def author_form(request, slug=None):
    if request.method == "POST":
        author = Author.objects.create(
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"), 
            country=request.POST.get("country"), 
            slug=request.POST.get("slug")
        )
        print("Author created:", author)
        return redirect("authors")
    
    # If GET request, render the form with the data
    fields = [
        {"name": "first_name", "label": "First Name"},
        {"name": "last_name", "label": "Last Name"},
        {"name": "country", "label": "Country"},
        {"name": "slug", "label": "Slug"},
    ]
    data = get_object_or_404(Author, slug=slug)  

    context = {"title": "Add new author", "fields": fields, "data": data, "mode": "view"}

    return render(request, "book_store/generic_form.html", context)

def author_detail(request, slug=None):
    author = get_object_or_404(Author, slug=slug)  # pk is the primary key, same as id
    return render(request, "book_store/generic_form.html", {"author": author})
