from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView
)
from rest_framework import permissions

from .models import Car, Owner
from .serailizers import CarSerializer, OwnerSerializer, RegisterSerializer

# _______________________CAR________________________


class CarListCreateView(ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated]


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        car = self.queryset.get(pk=self.kwargs["pk"])
        return car


# ____________________________Owner__________________________________

class RegisterView(CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer


class OwnerListCreateView(ListCreateAPIView):
    serializer_class = OwnerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Owner.objects.all()


class OwnerRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        owner = self.queryset.get(pk=self.kwargs["pk"])
        return owner
