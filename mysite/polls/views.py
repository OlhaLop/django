# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def page1(request):
    return HttpResponse("Page1.")

def page2(request):
    return HttpResponse("Page2")
