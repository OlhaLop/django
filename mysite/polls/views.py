# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from polls.models import User

def index(request):
    return render(request, 'polls/index.html')

def page1(request):
	rows = User.objects.all()
	context = {'rows': rows}
	return render(request, 'polls/page1.html', context)

def page2(request):
	rows = User.objects.filter(zipcode='5')
	context = {'rows': rows}
	return render(request, 'polls/page2.html', context)
