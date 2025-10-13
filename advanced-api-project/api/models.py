from django.db import models

class Author(models.Model): # Represents a writer who can have one or more published book
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    

#Each Author instance can be linked to multiple Book instances.
#This relationship is defined in the Book model using a ForeignKey.

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
#Represents a single book written by an Author.
#For example, you can access all books of an author using author.books.all()


    def __str__(self):
        return f"{self.title} ({self.publication_year})"

