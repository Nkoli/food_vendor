from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter

from .views.meal import MealViewSet
from .views.menu import MenuDetail, MenuList
from .views.order import (OrderDetail, OrderList)
from .views.user import UserRegisterViewSet, UserLoginViewSet, UserLogoutViewSet

router = DefaultRouter()
router.register(r'auth', UserRegisterViewSet, basename='register')
router.register(r'auth', UserLoginViewSet, basename='login')
router.register(r'auth', UserLogoutViewSet, basename='logout')
router.register(r'meals', MealViewSet, basename='meals')

urlpatterns = [
    path('', include(router.urls)),
    path('users/token/obtain/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('menus/', MenuList.as_view()),
    path('menus/<int:pk>/', MenuDetail.as_view()),
    path('orders/', OrderList.as_view()),
    path('orders/<int:pk>/', OrderDetail.as_view()),
]
