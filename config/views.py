from django.shortcuts import redirect


def index(request):
    # redirect to the book_outlet app index page
    return redirect("book_outlet/")
