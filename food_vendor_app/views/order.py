from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import Order
from ..serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)
