from django.contrib import admin

from .models import (DaysOfOccurence, Meal, Menu, Order, OrderPayment,
                     UserProfile, VendorProfile)

admin.site.register(UserProfile)
admin.site.register(VendorProfile)
admin.site.register(Meal)
admin.site.register(DaysOfOccurence)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(OrderPayment)
