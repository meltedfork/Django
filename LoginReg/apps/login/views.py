# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import *

# Create your views here.
def index(request):
    if 'userid' in request.session:
       return redirect("/success") 
    else:
        
        print 'error messages here from index'
        return render(request, 'login/index.html')

def register(request):
    errors = User.objects.validate(request.POST)
    print 'this process works', request.POST
    if len(errors) > 0:
        for error in errors:
            messages.error(request, error)
        return redirect("/")
    else:
        hashpwd = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt())
        newuser = User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=hashpwd)

        request.session['userid'] = newuser.id
        request.session['name'] = newuser.first_name
        print "session info", newuser.id, newuser.first_name
        return redirect("/success")

def login(request):
    # print postData['email']
    errors = User.objects.loginvalidate(request.POST)
    
    if len(errors) > 0:
        for error in errors:
            messages.error(request, error)
        return redirect("/")
    else:
        user = User.objects.filter(email=request.POST['email'])[0]
        request.session['userid'] = user.id
        request.session['name'] = user.first_name
        return redirect("/success")

def success(request):
    user = request.session['userid']
    return render(request, 'login/success.html')

def logout(request):
    request.session.clear()
    print 'goodbye'
    return redirect('/')   

