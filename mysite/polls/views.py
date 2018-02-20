# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request, 'polls/index.html')

def page1(request):
    return render(request, 'polls/page1.html')

def page2(request):
    return render(request, 'polls/page2.html')
