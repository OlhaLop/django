# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#test1 models
class User(models.Model):
    user = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=5)
    country = models.CharField(max_length=20, db_index=True)
    city = models.CharField(max_length=20)
    reg_date = models.DateTimeField('registration date', auto_now=True)
    years = models.IntegerField(default=0)

class Code(models.Model):
    zipcode = models.CharField(max_length=5)

#Many to one connection
class Manufacturer(models.Model):
	name = models.CharField(max_length=20)
	country = models.CharField(max_length=20)

	def __unicode__(self):
		return self.name

class Car(models.Model):
	manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
	name = models.CharField(max_length=20)

	def __unicode__(self):
		return self.name

#Many to many connection
class Topping(models.Model):
    name = models.CharField(max_length=20)
    mass = models.IntegerField()

    def __unicode__(self):
		return self.name

class Pizza(models.Model):
    toppings = models.ManyToManyField(Topping)
    name = models.CharField(max_length=20)

    def __unicode__(self):
		return self.name

# one to one connection
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __unicode__(self):              
        return self.name

class Restaurant(models.Model):
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __unicode__(self):
    	return self.place.name