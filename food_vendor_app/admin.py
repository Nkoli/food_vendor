from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (DaysOfOccurence, Meal, Menu, Order, OrderPayment,
                     UserProfile)
from .forms import UserProfileCreationForm, UserProfileChangeForm


class UserProfileAdmin(UserAdmin):
    add_form = UserProfileCreationForm
    form = UserProfileChangeForm
    model = UserProfile
    list_display = ['first_name', 'last_name', 'email', 'phone_number']


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Meal)
admin.site.register(DaysOfOccurence)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(OrderPayment)
