from __future__ import unicode_literals

from django.db import models
import re

class EmailManager(models.Manager):
    def validate_email(self, **kwargs):
        if re.search(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',kwargs['email_address']):
            email = Email.objects.create(email_address=kwargs['email_address'])
            return (True,email)
        else:
            return (False, "Not a valid email")

# Create your models here.
class Email(models.Model):
    email_address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = EmailManager()
