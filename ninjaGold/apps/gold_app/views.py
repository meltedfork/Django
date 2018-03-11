# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from random import randint
from time import strftime

def index(request):
    print "yup, working"
    
    if 'counter' not in request.session:
        request.session['counter'] = 0
    return render(request, 'gold_app/index.html')

def process(request):
    # response = 'we got to process'
    print 'post data??', request.POST
    print 'place:', request.POST['place']
    if 'activity' not in request.session:
        request.session['activity'] = []
    
    if 'Farm' in request.POST['place']:
         print 'farm works!'
         gold = randint(10, 20)
         print 'farm gold', gold
         request.session['counter'] += gold
         activity_str = 'Earned ' + str(gold) + ' gold from The Farm!' + (strftime("%B %d, %Y %I:%M %p %Z"))
         print 'working str??', activity_str
         request.session['activity'].append(activity_str)

    if 'Cave' in request.POST['place']:
        gold = randint(5, 10)     
        request.session['counter'] += gold
        activity_str = 'Earned ' + str(gold) + ' gold from The Cave!' + (strftime("%B %d, %Y %I:%M %p %Z"))
        request.session['activity'].append(activity_str)

    if 'House' in request.POST['place']:
        gold = randint(2, 5)     
        request.session['counter'] += gold
        activity_str = 'Earned ' + str(gold) + ' gold from The House!' + (strftime("%B %d, %Y %I:%M %p %Z"))
        request.session['activity'].append(activity_str)

    if 'Casino' in request.POST['place']:
        gold = randint(-50, 50)
        print 'casino gold', gold 
        request.session['counter'] += gold
        if gold >= 0:
            activity_str = 'Earned ' + str(gold) + ' gold from The Casino!' + (strftime("%B %d, %Y %I:%M %p %Z"))
            request.session['activity'].append(activity_str)
        else:
            activity_str = 'In The Casino, you lost ' + str(gold) + '...Ouch..' + (strftime("%B %d, %Y %I:%M %p %Z"))
            request.session['activity'].append(activity_str) 
    
    return redirect('/')

def reset(request):
    request.session.clear()

    print 'reset session success!'
    print 'cleared session:', request.session
    return redirect('/')