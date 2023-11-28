from django.db import models
from datetime import date


class ShowManager(models.Manager):
    def validator(self, data_from_POST):
        errors = {}
        # x = Show.objects.get(title=data_from_POST['title'])

        if len(data_from_POST['title']) < 2:
            errors['title'] = "Title should be at least 2 characters"       
        if Show.objects.filter(title=data_from_POST['title']):             #true only if title exists, we cannot use .get here (filter always returns list empty or not) empty list returns false for this if
            errors['title_exsist'] = "this book alredy exists, Try different title!"
        if len(data_from_POST['network']) < 3:
            errors['network'] = "network name should be at least 3 characters"
        if data_from_POST['date'] > str(date.today()):
            errors['date'] = "how the hell this TV show released in future??"
        if data_from_POST['desc']:
            if len(data_from_POST['desc']) < 10:
                errors['desc'] = "description is optional, if added it must be at least 10 chars"
        return errors



class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    date = models.DateField()
    desc = models.TextField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = ShowManager()
