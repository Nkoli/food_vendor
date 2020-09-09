from django.urls import path

from .views.meal import MealDetail, MealList
from .views.menu import MenuDetail, MenuList
from .views.order import (OrderDetail, OrderList)
from .views.user import UserRegistrationView

urlpatterns = [
    path('users/register/', UserRegistrationView.as_view()),
    path('meals/', MealList.as_view()),
    path('meals/<int:pk>/', MealDetail.as_view()),
    path('menus/', MenuList.as_view()),
    path('menus/<int:pk>/', MenuDetail.as_view()),
    path('orders/', OrderList.as_view()),
    path('orders/<int:pk>/', OrderDetail.as_view()),
]
