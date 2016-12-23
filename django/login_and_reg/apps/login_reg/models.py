from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ObjectDoesNotExist
import re
import bcrypt

# Create your models here.

class UserManager(models.Manager):
    def validate_login(self, **kwargs):
        print "Made it into the user login validation"
        errors = []
        try:
            query = User.objects.get(email=kwargs['email_address'])
            if bcrypt.hashpw(kwargs['password'].encode('utf-8'),query.password.encode('utf-8')) == query.password:
                #we found and matched the password
                return (True,query)
            else:
                errors.append('Password is incorrect')
                return (False,errors)
        except ObjectDoesNotExist:
            errors.append(str(kwargs['email_address'])+' does not exist in the database.')
            return (False,errors)

    def validate_registration(self, **kwargs):
        print "Made it into the user registration validation"
        errors = []
        NAME_REGEX = re.compile(r'[a-zA-Z_-]+$')
        #check first name
        if len(kwargs['first_name']) < 2:
            errors.append('First name cannot be less than two characters.')
        if not NAME_REGEX.match(kwargs['first_name']):
            errors.append('Your first name can\'t contain any thing but letters silly.')

        #check last name
        if len(kwargs['last_name']) < 2:
            errors.append('Last name cannot be less than two characters.')
        if not NAME_REGEX.match(kwargs['last_name']):
            errors.append('Your last name can\'t contain any thing but letters silly.')

        #regex: email verification stirng
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
        #check email
        if len(kwargs['email_address']) < 1:
            errors.append('We would really like to spam your inbox, please provide your email')
        if not EMAIL_REGEX.match(kwargs['email_address']):
            errors.append('This is not a valid email, try again!')
        try:
            query = User.objects.get(email=kwargs['email_address'])
            if query.email:
                errors.append('Email address already exists in the database.')
        except ObjectDoesNotExist:
            # pass, means users email is not in the DB already
            pass


        #check password length
        if len(kwargs['password']) < 8 or len(kwargs['confirm_password']) < 8:
            errors.append('Password must be a minimum of 8 characters long.')
        else: #check hash of password = hash of confirm password
            pw_hash = bcrypt.hashpw(kwargs['password'].encode('utf-8'),bcrypt.gensalt())
            if bcrypt.hashpw(kwargs['confirm_password'].encode('utf-8'),pw_hash) != pw_hash:
                errors.append('Passwords do not match')

        if not errors:
            user = User.objects.create(first_name=kwargs['first_name'],last_name=kwargs['last_name'],email=kwargs['email_address'],password=pw_hash)
            return (True,user)
        else:
            return (False,errors)

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
