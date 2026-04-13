from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
    CreateAPIView,
)

from .models import Car, Owner
from .serailizers import CarSerializer, OwnerSerializer

# _______________________________________________


class CarListView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


# class CarRetrieveView(RetrieveAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer


# class CarCreateView(CreateAPIView):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer


# ________________________________________________


class CarListCreateView(ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get_object(self):
        car = self.queryset.get(pk=self.kwargs["pk"])
        return car


# ____________________________Owner__________________________________


class OwnerListView(ListAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


# class OwnerRetrieveView(RetrieveAPIView):
#     queryset = Owner.objects.all()
#     serializer_class = OwnerSerializer


# class OwnerCreateView(CreateAPIView):
#     queryset = Owner.objects.all()
#     serializer_class = OwnerSerializer

# ___________________________________________________________________________


class OwnerListCreateView(ListCreateAPIView):
    serializer_class = OwnerSerializer

    def get_queryset(self):
        return Owner.objects.all()


class OwnerRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    
    def get_object(self):
        owner = self.queryset.get(pk=self.kwargs["pk"])
        return owner
