from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter

from .views.meal import MealDetail, MealList
from .views.menu import MenuDetail, MenuList
from .views.order import (OrderDetail, OrderList)
from .views.user import UserRegisterViewSet, UserLoginViewSet, UserLogoutViewSet

router = DefaultRouter()
router.register(r'auth', UserRegisterViewSet, basename='register')
router.register(r'auth', UserLoginViewSet, basename='login')
router.register(r'auth', UserLogoutViewSet, basename='logout')

urlpatterns = [
    path('', include(router.urls)),
    path('users/token/obtain/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('meals/', MealList.as_view()),
    path('meals/<int:pk>/', MealDetail.as_view()),
    path('menus/', MenuList.as_view()),
    path('menus/<int:pk>/', MenuDetail.as_view()),
    path('orders/', OrderList.as_view()),
    path('orders/<int:pk>/', OrderDetail.as_view()),
]
