from django.db import models
import re
from datetime import date


class UserManager(models.Manager):
    def validator(self,POST_data):
        errors = {}
        if len(POST_data['first_name']) < 4:                                        #first name length
            errors['first_name'] = 'your first name should be at least 4 characters'

        if len(POST_data['last_name']) < 4:                                         #last name length
            errors['last_name'] = 'your last name should be at least 4 characters'

        if User.objects.filter(email = POST_data['email']):                         #account already exists? unique email
            errors['account_exsits'] = 'email address used for another account!'

        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')  #email syntax valid?
        if not email_regex.match(POST_data['email']):
            errors['vaild_email'] = "Invalid email address!"

        if len(POST_data['password']) < 8:                                          #password length 8
            errors['password_len'] = 'your password should be at least 8 characters'

        if POST_data['password_2'] != POST_data['password']:                        #password confirmation
            errors['password_confirm'] = 'password and password confirmation does not match!'

        if POST_data['birth_day'] > str(date.today()):                              #birth day in the past
            errors['person_not_borned']= 'you were not borned yet madafaka!'

        if int(POST_data['birth_day'][0:4]) + 13 > int(str(date.today())[0:4]):     #age +13 only allowed
            errors['too_young'] = 'your just a baby this website is +13'
        
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    birth_day = models.DateField()
    objects = UserManager()
