# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request, methods='POST'):
    print "here we go!"
    return render(request, "surveys_app/index.html")

def process(request):
    print "received data"
    if request.session['context'] == request.session['context'] and 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1    

    request.session['context'] = {
        'name': request.POST['name'],
        'location': request.POST['location'],
        'language': request.POST['language'],
        'comment': request.POST['comment']
    }
    
    print "this works too", request.session['context']
    return redirect('/result', request)  

def result(request):
    print "we got this far"
    
    print "post data:", request.session['context']
    #print context 
    return render(request, "surveys_app/result.html")