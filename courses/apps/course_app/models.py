# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login.models import User
# need to link each apps models
# Create your models here.
class CourseManager(models.Manager):
    def validate(self, postData):
        errors = {}
        if len(postData['course_name']) < 1:
            errors['Please enter a course name'] = 'course_name'

        if len(postData['description']) < 1:
            errors['Description can not be blank'] = 'description'

        return errors      

class Course(models.Model):
    course_name = models.CharField(max_length=45)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ManyToManyField(User, related_name='admin')
    updated_at = models.DateTimeField(auto_now=True)
    

    objects = CourseManager()    