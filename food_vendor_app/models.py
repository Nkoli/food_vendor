from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserProfileManager


class UserProfile(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserProfileManager()

    is_vendor = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name}'


class VendorProfile(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE,
                                related_name='vendor_profile')
    business_name = models.CharField(max_length=100)


class Meal(models.Model):
    name = models.CharField(max_length=300)
    vendor = models.ForeignKey(VendorProfile, on_delete=models.CASCADE, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} made by {self.vendor_id.first_name}'


class DaysOfOccurence(models.Model):
    WEEKLY_CHOICES = [
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THUR', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
        ('SUN', 'Sunday'),
    ]
    name = models.CharField(max_length=4, choices=WEEKLY_CHOICES)

    def __str__(self):
        return self.name


class Menu(models.Model):
    MENU_TYPE = [
        ('VEGAN', 'Vegan'),
        ('VEGETARIAN', 'Vegetarian'),
        ('NON-VEGAN', 'Non-Vegan'),
        ('GLUTEN-FREE', 'Gluten-Free'),
        ('DAIRY-FREE', 'Dairy-Free')
    ]

    vendor = models.ForeignKey(VendorProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    meals = models.ManyToManyField(Meal)
    menu_type = models.CharField(max_length=20, choices=MENU_TYPE)
    frequency_of_reoccurence = models.SmallIntegerField()
    days_of_reoccurence = models.ManyToManyField(DaysOfOccurence)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}, a {self.menu_type} menu.'


class Order(models.Model):
    customer = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                                 related_name='customer_user')
    vendor = models.ForeignKey(VendorProfile, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True, blank=True)
    meals = models.ForeignKey(Meal, on_delete=models.CASCADE, null=True, blank=True)


class OrderPayment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount_due = models.DecimalField(max_digits=8, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=8, decimal_places=2)
    amount_outstanding = models.DecimalField(max_digits=8, decimal_places=2)
