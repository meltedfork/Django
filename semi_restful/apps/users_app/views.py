# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
    # print 'here is index'
    #context pulls db info into table
    context = {
        'users': User.objects.all() 
    }
    return render(request, 'users_app/index.html', context)

def new(request):
    print 'this is new user page'
    return render(request, 'users_app/new_user.html')  

def edit(request, id):
    print 'will bring up edit.html template'
    # gets specific id of user to edit
    user = User.objects.get(id=id)
    context = {
        'user': user
    }
    return render(request, 'users_app/edit.html', context)

def show(request, id):
    print 'show method works!'
    # gets specific id of user to display info
    user = User.objects.get(id=id)
    context = {
        'user': user
    }
    return render(request, 'users_app/show_user.html', context)

def create(request, methods='POST'):
    print request.POST
    errors = User.objects.validate(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect('/users/{{user.id}}/edit')
    else:    
        User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email']
        )
    #database function to add user into database
    return redirect('/users/')

def update(request, id):
    
    errors = User.objects.validate(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect('/users/{{user.id}}/edit')
    else:
        user = User.objects.get(id =id)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        return redirect('/users/'+id)

def destroy(request, id):
    User.objects.get(id = id).delete()
    return redirect('/users')
