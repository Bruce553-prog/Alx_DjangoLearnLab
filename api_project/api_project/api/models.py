from django.db import models
class Book(models.Model):
    tittle=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    
