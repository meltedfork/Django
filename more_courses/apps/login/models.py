# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import bcrypt, re

# Create your models here.
class UserManager(models.Manager):
    def validate(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["First name can not be blank"] = "first_name"
        
        if len(postData['last_name']) < 2:
            errors["Last name can not be blank"] = "last_name"  
        
        if len(postData['email']) < 1:
            errors["Email field can not be blank"] = "email"
        
        if (User.objects.filter(email=postData['email'])):
            errors['Email already in use'] = "email"

        if len(postData["password"]) < 8:
            hashpwd = bcrypt.hashpw(postData["password"].encode(), bcrypt.gensalt())
            # set old password to hashpwd and save to db, BUT HOW?    
            errors["Password must be at least 8 characters" ] = "password"

        if postData["password"] != postData["password2"]:
            errors["Passwords do not match"] = "password2"  
        
        return errors

    def loginvalidate(self, postData): # check db email with submitted email
        # print postData['email']
        errors = {}
        
        if len(postData['email']) < 1:
            errors["Email field can not be blank"] = "email"

        if len(postData["password"]) < 8:
            errors["Password must be at least 8 characters" ] = "password"

        if (User.objects.filter(email=postData['email'])):
            print 'TRUE for emails'
            currentuser = User.objects.get(email=postData['email'])
            existingpwd = currentuser.password
        
            if not bcrypt.checkpw(postData["password"].encode(), existingpwd.encode()):
                errors["Password does not match"] = "password"
        else:
            errors["Email does not match"] = "email"
        
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # *************************
    # Connect an instance of UserManager to our User model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    objects = UserManager()