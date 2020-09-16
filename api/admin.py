from django.contrib import admin

from .models import User, Meal, Menu, Order, OrderPayment, Days_Of_Occurence

admin.site.register(Days_Of_Occurence)
admin.site.register(User)
admin.site.register(Meal)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(OrderPayment)
