from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from .models import Car, Owner
from .serailizers import CarSerializer, OwnerSerializer


class CarView(APIView):
    def get_car(self, pk):
        car = Car.objects.filter(pk=pk).first()

        if not car:
            raise NotFound(detail="car topilmadi")

        return car

    def get(self, request, pk=None):

        if pk:
            car = self.get_car(pk=pk)

            serializer = CarSerializer(car)

            return Response(serializer.data)

        cars = Car.objects.all()

        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

    def post(self, request, pk=None):
        serializer = CarSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Ma'lumot muavvaqiyatli saqlandi!!!"})

    def put(self, request, pk=None):
        car = self.get_car(pk)

        serializer = CarSerializer(instance=car, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"message": "Ma'lumot muavvaqiyatli yangilandi!!!"})

    def patch(self, request: Request, pk=None):

        car = self.get_car(pk)

        serializer = CarSerializer(instance=car, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"message": "Ma'lumot muavvaqiyatli yangilandi!!!"})

    def delete(self, request, pk=None):
        car = self.get_car(pk)

        car.delete()

        return Response({"message": "Ma'lumotlar o'chirildi"})


class OwnerView(APIView):
    def get_owner(self, pk):
        owner = Owner.objects.filter(pk=pk).first()
        if not owner:
            raise NotFound(detail="owner topilmadi")
        return owner

    def get(self, request, pk=None):

        if pk:
            owner = self.get_owner(pk=pk)

            serializer = OwnerSerializer(owner)

            return Response(serializer.data)

        owners = Owner.objects.all()

        serializer = OwnerSerializer(owners, many=True)
        return Response(serializer.data)

    def post(self, request, pk=None):
        serializer = OwnerSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Ma'lumot muavvaqiyatli saqlandi!!!"})

    def put(self, request, pk=None):
        owner = self.get_owner(pk)

        serializer = OwnerSerializer(instance=owner, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"message": "Ma'lumot muavvaqiyatli yangilandi!!!"})

    def patch(self, request: Request, pk=None):

        owner = self.get_owner(pk)

        serializer = OwnerSerializer(instance=owner, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"message": "Ma'lumot muavvaqiyatli yangilandi!!!"})

    def delete(self, request, pk=None):
        owner = self.get_owner(pk)

        owner.delete()

        return Response({"message": "Ma'lumotlar o'chirildi"})
