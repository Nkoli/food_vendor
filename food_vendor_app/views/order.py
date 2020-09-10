from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from ..models import Order, OrderPayment
from ..serializers import OrderPaymentSerializer, OrderSerializer


class OrderList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class OrderDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        order = self.get_object(pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, pk):
        order = self.get_object(pk)
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        order = self.get_object(pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderPaymentList(APIView):
    def get(self, request):
        order_payments = OrderPayment.objects.all()
        serializer = OrderPaymentSerializer(order_payments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderPaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class OrderPaymentDetail(APIView):
    def get_object(self, pk):
        try:
            return OrderPayment.objects.get(pk=pk)
        except OrderPayment.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        order_payment = self.get_object(pk)
        serializer = OrderPaymentSerializer(order_payment)
        return Response(serializer.data)

    def put(self, request, pk):
        order_payment = self.get_object(pk)
        serializer = OrderPaymentSerializer(order_payment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        order_payment = self.get_object(pk)
        order_payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
