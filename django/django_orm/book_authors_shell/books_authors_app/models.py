from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
#   authors = imaginary field to represnt related name     

class Author(models.Model):
    books = models.ManyToManyField(Book, related_name='authors', null=True)
    note = models.TextField()
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


#cuz this is many to many we can say that Author objects now can access books (also Book objects can now access authors)