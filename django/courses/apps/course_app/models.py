from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def validate_course(self, **kwargs):
        errors = []
        if not kwargs['name']:
            errors.append('You must fill in a course name')
        if not kwargs['description']:
            errors.append('You must have a course description')

        if not errors:
            course = Course.objects.create(name=kwargs['name'],description=kwargs['description'])
            return (True, course)
        else:
            return (False, errors)

class Course(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CourseManager()
