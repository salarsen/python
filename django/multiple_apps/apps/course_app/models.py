from __future__ import unicode_literals

from django.db import models
from ..login_reg.models import User
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from django.db.models import Count
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


class EnrolledManager(models.Manager):
    def enroll_user(self, **kwargs):
        print "here" + str(kwargs['user'])
        errors = []
        if int(kwargs['user']) == 0:
            errors.append('You did not select a valid user')
        if int(kwargs['course']) == 0:
            errors.append('You did not select a valid course')

        if not errors:
            try:
                user = User.objects.get(id=kwargs['user'])
            except ObjectDoesNotExist:
                errors.append('Unable to find user')
            try:
                course = Course.objects.get(id=kwargs['course'])
            except ObjectDoesNotExist:
                errors.append('Unable to find course')
            # re-verify no errors from fetch queries
            if not errors:
                try:
                    enrolled_chk = Enrolled.objects.get(user=user,course=course)
                    errors.append("User already enrolled in this class")
                    return (False,errors)
                except MultipleObjectsReturned:
                    errors.append("User already enrolled in this class")
                    return (False,errors)
                except ObjectDoesNotExist:
                    enrolled = Enrolled.objects.create(user=user,course=course)
                    return (True,enrolled)
            else:
                return (False,errors)
        else:
            return (False,errors)

    def class_size(self):
        class_info = []
        classes = Enrolled.objects.values_list('course').annotate(num_students=Count('user')).all()
        for unique_class in classes:
            try:
                class_name = Enrolled.objects.get(id=int(unique_class[0])).course.name
            except ObjectDoesNotExist:
                class_name = "NA"
            class_info.append({'course':unique_class[0],'name':class_name,'num_students':unique_class[1],})

        return class_info

# the other option here is to do a ManyToManyField in course
class Enrolled(models.Model):
    user = models.ForeignKey(User,null=True)
    course = models.ForeignKey(Course,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = EnrolledManager()
