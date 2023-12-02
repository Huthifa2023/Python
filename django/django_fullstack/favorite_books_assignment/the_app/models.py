from django.db import models
import re

class UserManager(models.Manager):
    def validator(self,post_data):
        errors = {}
        if len(post_data['first_name']) < 2:
            errors['first_name'] = 'your first name should be at least 4 characters'
        if len(post_data['last_name']) < 2:
            errors['last_name'] = 'your last name should be at least 4 characters'
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not email_regex.match(post_data['email']):
            errors['email'] = 'make sure your email is valid'
        if len(post_data['password']) < 8:
            errors['password_length'] = 'your password must be at least 8 characters'
        if post_data['password'] != post_data['password2']:
            errors['pass-confirm'] = 'your password confirmation does not match'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()
    #created_books = ##
    #liked_books = ##

####################################################################################

class BookManager(models.Manager):
    def validator(self, post_data):
        errors = {}
        if len(post_data['desc']) < 5:
            errors['desc'] = 'the description must be at least 5 chracters'
        return errors
    
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()

    created_by = models.ForeignKey(User, related_name='created_books', on_delete=models.CASCADE)
    liked_by = models.ManyToManyField(User, related_name='liked_books')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = BookManager()