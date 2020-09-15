from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from ..models import Meal
from ..permissions import IsOwnerOrReadOnly
from ..serializers import MealSerializer


class MealViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    def perform_create(self, serializer):
        serializer.save(vendor=self.request.user)
