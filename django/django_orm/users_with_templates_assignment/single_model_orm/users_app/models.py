from django.db import models

class User(models.Model):
    def __str__(self):
        return f"<Movie object: {self.title} ({self.id})>"  #the shell to display multi objects correctly
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

