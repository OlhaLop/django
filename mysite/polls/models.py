# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#test1 models
class User(models.Model):
    user = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=5)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)

class Code(models.Model):
    zipcode = models.CharField(max_length=5)