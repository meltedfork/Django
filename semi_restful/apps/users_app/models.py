# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def validate(self, postData):
        errors = {}
        if len(postData['first_name']) < 3:
            errors["first_name"] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 3:
            errors["last_name"] = "Last name should be at least 2 characters"    
        if len(postData['email']) < 0:
            errors["email"] = "Email field can not be blank"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45, default = 'blank')
    last_name = models.CharField(max_length=45, default = 'blank')
    email = models.CharField(max_length=45, default = 'blank')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # *************************
    # Connect an instance of UserManager to our User model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    objects = UserManager()