import datetime

# from django.contrib.auth import logout
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from ..serializers import UserLoginSerializer, UserRegisterSerializer
from ..utils import create_user_account, get_and_authenticate_user


def get_tokens_for_user(user_object):
    refresh = RefreshToken.for_user(user_object)
    access_token = refresh.access_token
    access_token.set_exp(lifetime=datetime.timedelta(minutes=500))
    return {
        'refresh': str(refresh),
        'access': str(access_token)
    }


class UserRegisterViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    serializer_class = UserRegisterSerializer

    @action(methods=['POST', ], detail=False)
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = create_user_account(**serializer.validated_data)
        token = get_tokens_for_user(user)
        data = UserRegisterSerializer(user).data
        return Response(
            {
                "data": data,
                "token": token
            },
            status=status.HTTP_201_CREATED
        )


class UserLoginViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    @action(methods=['POST', ], detail=False)
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_and_authenticate_user(**serializer.validated_data)
        token = get_tokens_for_user(user)
        data = UserLoginSerializer(user).data
        return Response(
            {
                "data": data,
                "token": token
            },
            status=status.HTTP_200_OK
        )


# class UserLogoutViewSet(viewsets.GenericViewSet):
#     permission_classes = [IsAuthenticated]

#     @action(methods=['POST', ], detail=False)
#     def logout(self, request):
#         logout(request)
#         return Response(
#             {
#                 "message": "Successfully logged out"
#             }, status=status.HTTP_200_OK
#         )
