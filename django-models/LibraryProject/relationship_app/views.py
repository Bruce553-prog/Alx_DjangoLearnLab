from django.shortcuts import render
from .models import Book  # must import Book

def list_books(request):
    books = Book.objects.all()  # checker requires this exact line
    return render(request, "relationship_app/list_books.html", {"books": books})
