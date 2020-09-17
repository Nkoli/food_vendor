from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class User(AbstractUser):

    username = None
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    name = models.CharField(max_length=200, blank=False, null=False)
    is_vendor = models.BooleanField(default=False)
    business_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.email} - {self.name}'


class Meal(models.Model):
    name = models.CharField(max_length=300)
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    metadata = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} made by {self.vendor.name}'


class Days_Of_Occurence(models.Model):
    DAYS = [
        ('MONDAY', 'Monday'),
        ('TUESDAY', 'Tuesday'),
        ('WEDNESDAY', 'Wednesday'),
        ('THURSDAY', 'Thursday'),
        ('FRIDAY', 'Friday'),
        ('SATURDAY', 'Saturday'),
        ('SUNDAY', 'Sunday')
    ]

    days_of_occurence = models.CharField(
        max_length=15, choices=DAYS, unique=True)

    def __str__(self):
        return self.days_of_occurence


class Menu(models.Model):
    DIETARY_TYPE = [
        ('VEGAN', 'Vegan'),
        ('VEGETARIAN', 'Vegetarian'),
        ('NON-VEGAN', 'Non-Vegan'),
        ('GLUTEN-FREE', 'Gluten-Free'),
        ('DAIRY-FREE', 'Dairy-Free')
    ]

    name = models.CharField(max_length=200)
    meals = models.ManyToManyField(Meal, related_name='meals')
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)
    dietary_type = models.CharField(max_length=20, choices=DIETARY_TYPE)
    description = models.TextField(null=True)
    days_of_occurence = models.ManyToManyField(Days_Of_Occurence, related_name='days')
    frequency_of_occurence = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}, a {self.dietary_type} menu.'


class Order(models.Model):
    ORDER_STATUS = [
        ('PENDING_FULLY_PAID', 'pending_fully_paid'),
        ('DELIVERED_FULLY_PAID', 'delivered_fully_paid'),
        ('PENDING', 'pending'),
        ('DELIVERED', 'delivered')
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_user')
    vendor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vendor_user')
    status = models.CharField(max_length=25, choices=ORDER_STATUS)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True, blank=True)
    meal = models.ManyToManyField(Meal, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class OrderPayment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_payment')
    amount_due = models.DecimalField(max_digits=8, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=8, decimal_places=2)
