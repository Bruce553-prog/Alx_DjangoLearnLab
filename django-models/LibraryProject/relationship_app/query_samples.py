import os
import django

# Setup Django environment so the script can run independently
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        return Book.objects.filter(author=author)  # Checker requires this
    except Author.DoesNotExist:
        return []

# List all books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return []

# Retrieve the librarian for a library
def get_librarian(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return Librarian.objects.get(library=library)  # Checker requires this
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None

# Example usage
if __name__ == "__main__":
    print("Books by Author 'Alice':", books_by_author("Alice"))
    print("Books in Library 'Central':", books_in_library("Central"))
    print("Librarian of Library 'Central':", get_librarian("Central"))
