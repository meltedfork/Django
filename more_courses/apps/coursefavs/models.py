# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from datetime import date, datetime, timedelta, time
from ..login.models import User

# Create your models here.

class CourseManager(models.Manager):
    def validate(self, postData):
        print 'course.model: validate: postData', postData
        errors = []

        if len(postData['name']) < 5:
            errors.append("Course name must be more than 5 characters")

        if len(postData['description']) < 15:
            errors.append("Course description must be longer than 15 characters") 

        print 'here are the errors: ', errors   
        return errors



class Course(models.Model):
    name = models.CharField(max_length = 45)
    description = models.CharField(max_length = 100)
    favorite = models.ManyToManyField(User, related_name='upvote')
    created_by = models.ForeignKey(User, related_name='admin')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)        

    objects = CourseManager()

  