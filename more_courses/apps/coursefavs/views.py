# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import date, datetime, timedelta, time
from .models import Course
from ..login.models import User



def index(request):
    print 'index in courses'

    userid = request.session['userid']
    print 'person in session: userid: ', userid

    user = User.objects.get(id=userid)     # variable 'user' equals the db info for a user filtered to match the current user in session by comparing session userid w db user.id
    favorite = user.upvote.all()        # variable 'favorite' is all 'liked' courses (upvoted) by currentuser (aka in session)
    mycourses = Course.objects.all().exclude(favorite=user)     # variable 'mycourses' is all the courses from db  
                                                                # .exclude makes course that is favorited to disappear from general list
    
    print 'course info in index: ', mycourses

    context = {                                 # use context to pass info to template for displaying
        'mycourses': mycourses,
        'favorite': favorite
    }
    return render(request, 'coursefavs/courselist.html', context)  



def new(request):
    print 'new in courses'
    return render(request, 'coursefavs/courseadd.html')    




def create(request):
    print 'this is request.POST data in courses create: ', request.POST
    errors = Course.objects.validate(request.POST)
    
    if len(errors) > 0:
        print 'this is for errors'
        for error in errors:
            messages.error(request, error)
        return redirect('/courses/new')

    else:
        print 'this is for no errors'
        userid = request.session['userid']
        user = User.objects.get(id=userid)
        print 'user in courses create:', user
        Course.objects.create(
            name=request.POST['name'],
            description=request.POST['description'],
            created_by=user)

        return redirect('/courses/')



    
def favorite(request, id):
    print 'favorite in courses view'
    # passed course id when clicked on fav link, myfav var to make sure right course info from in session userid, add to db in favorite
    userid = request.session['userid']
    myfav = Course.objects.get(id=id)
    myfav.favorite.add(userid)      # part of many-to-many relationship
    myfav.save()                    # save specific course to favorite
    return redirect('/courses/')         


def popfavback(request, id):
    print 'need to develop this logic'    # opposite from adding to fav...this removes specific course from favorite
    userid = request.session['userid']
    myfav = Course.objects.get(id=id)
    myfav.favorite.remove(userid)
    myfav.save()
    return redirect('/courses/')


def remove(request, id):
    userid = request.session['userid']
    course = Course.objects.get(id=id)
    print'course.created_by_id info:', course.created_by_id
    if course.created_by_id == userid:
        print 'we are getting close to removing it'
        return redirect('/courses/'+id+'/delete')
        
    else:
        print 'need to show remove error'
        error = 'unauthorized user. you may only delete courses you created'
        messages.error(request, error)
       
        print 'remove: messages', messages
        return redirect('/courses/')   
    


def delete(request, id):
    print 'delete in courses view'
    destroy_course = Course.objects.get(id=id)
    destroy_course.delete()
    return redirect('/courses/')


def logout(request):
    request.session.clear()
    print 'goodbye'
    return redirect('/')   

    