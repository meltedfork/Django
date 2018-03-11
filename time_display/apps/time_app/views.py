# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
# Create your views here.

def index(request):
    context = {
        "time": strftime("%B %d, %Y %I:%M %p %Z", gmtime())
    }
    return render(request,'time_app/index.html', context)

def time_display(request):
    return redirect('/') 
