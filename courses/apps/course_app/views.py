# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime, localtime
from ..login.models import User

# Create your views here.
def courses(request):
    response = 'having fun yet??'
    print 'session info', request.session['userid']
    user = User.objects.filter(id=request.session['userid'])[0]
    
    print 'first name?', user.first_name

    return HttpResponse(response)


def time(request):
    context = {
    'time': strftime('%Y-%m-%d %H:%M %p', localtime())
    }
    return render(request, "beltapp/index.html", context) 