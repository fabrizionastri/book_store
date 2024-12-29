from django.shortcuts import redirect


def index(request):
    # redirect to the book_store app index page
    return redirect("book_store/")
