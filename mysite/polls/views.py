# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from polls.models import User, Manufacturer, Pizza, Restaurant

def index(request):
    return render(request, 'polls/index.html')

def page1(request):

	# SELECT ALL
	rows1 = User.objects.all()
	
	"""different filters applied"""

	#filter by time
	rows2 = User.objects.filter(reg_date__contains='5:59')
	
	#filter by range
	rows3 = User.objects.filter(years__range=(22, 27)).order_by('years').reverse()
	
	#converting results to appropriate format
	context = {'rows1': rows1,
			   'rows2': rows2,
			   'rows3': rows3	}
	return render(request, 'polls/page1.html', context)

def page2(request):

	#filter by defined field
	rows = User.objects.filter(zipcode='5')
	
	"""filters to connected odjects applied"""

	#many to one
	res = Manufacturer.objects.filter(car__name__contains='g')
	
	#many to many
	res1 = Pizza.objects.filter(toppings__name='sausage').filter(toppings__name='cheese')
	
	#one to one
	res2 = Restaurant.objects.filter(place__address='ppp')

	#converting results to appropriate format
	context = {'rows': rows,
				'res':res,
				'res1':res1,
				'res2':res2 }
	return render(request, 'polls/page2.html', context)
