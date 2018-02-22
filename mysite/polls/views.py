# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from polls.models import User

from datetime import datetime, timedelta

def index(request):
    return render(request, 'polls/index.html')

def page1(request):
	
	rows1 = User.objects.all()
	rows2 = User.objects.filter(reg_date__contains='5:59')
	rows3 = User.objects.filter(years__range=(22, 27))
	context = {'rows1': rows1,
			   'rows2': rows2,
			   'rows3': rows3	}
	return render(request, 'polls/page1.html', context)

def page2(request):
	rows = User.objects.filter(zipcode='5')
	context = {'rows': rows}
	return render(request, 'polls/page2.html', context)
