from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        return author.books.all()
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
        return library.librarian
    except Library.DoesNotExist:
        return None

# Example usage
if __name__ == "__main__":
    print("Books by Author 'Alice':", books_by_author("Alice"))
    print("Books in Library 'Central':", books_in_library("Central"))
    print("Librarian of Library 'Central':", get_librarian("Central"))
