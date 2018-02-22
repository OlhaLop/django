# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import User, Code, Manufacturer, Car, Topping, Pizza, Place, Restaurant

admin.site.register(User)
admin.site.register(Code)
admin.site.register(Manufacturer)
admin.site.register(Car)
admin.site.register(Topping)
admin.site.register(Pizza)
admin.site.register(Place)
admin.site.register(Restaurant)