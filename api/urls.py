from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter

from .views.meal import MealViewSet
from .views.menu import MenuViewSet
from .views.order import OrderList, OrderDetail, PaymentList, PaymentDetail
from .views.user import UserRegisterViewSet, UserLoginViewSet, UserLogoutViewSet

router = DefaultRouter()
router.register(r'auth', UserRegisterViewSet, basename='register')
router.register(r'auth', UserLoginViewSet, basename='login')
router.register(r'auth', UserLogoutViewSet, basename='logout')
router.register(r'meals', MealViewSet, basename='meals')
router.register(r'menus', MenuViewSet, basename='menus')

urlpatterns = [
    path('', include(router.urls)),
    path('users/token/obtain/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('orders/', OrderList.as_view()),
    path('orders/<int:pk>/', OrderDetail.as_view()),
    path('payments/', PaymentList.as_view()),
    path('payments/<int:pk>/', PaymentDetail.as_view()),
]
