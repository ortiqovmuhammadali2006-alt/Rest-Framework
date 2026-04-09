from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from .models import Car


class CarView(APIView):
    def get(self, request: Request, pk=None):
        if pk is not None:
            car = Car.objects.filter(pk=pk).values().first()
            if not car:
                raise NotFound(detail=f"{pk}-id li avtomobil topilmadi")
            return Response(car)

        cars = list(Car.objects.values())
        return Response(cars)

    def post(self, request: Request):
        body = request.data
        Car.objects.create(**body)
        return Response({"message": "Avtomobil muvaffaqiyatli qo'shildi"})

    def put(self, request: Request, pk):
        car = Car.objects.filter(pk=pk).first()
        if not car:
            raise NotFound(detail=f"{pk}-id li avtomobil topilmadi")

        body = request.data

        car.name = body.get("name", car.name)
        car.brand = body.get("brand", car.brand)
        car.color = body.get("color", car.color)
        car.year = body.get("year", car.year)
        car.price = body.get("price", car.price)
        car.is_available = body.get("is_available", car.is_available)
        car.save()

        return Response({"message": "Avtomobil ma'lumotlari yangilandi"})
    
    def patch(self, request: Request, pk):
        car = Car.objects.filter(pk=pk).first()
        if not car:
            raise NotFound(detail=f"{pk}-id li avtomobil topilmadi")

        body = request.data

        car.name = body.get("name", car.name)
        car.brand = body.get("brand", car.brand)
        car.color = body.get("color", car.color)
        car.year = body.get("year", car.year)
        car.price = body.get("price", car.price)
        car.save()

        return Response({"message": "Avtomobil ma'lumotlari yangilandi"})

    def delete(self, request: Request, pk):
        car = Car.objects.filter(pk=pk).first()
        if not car:
            raise NotFound(detail=f"{pk}-id li avtomobil topilmadi")

        car.delete()
        return Response({"message": "Avtomobil o'chirildi"})
    

##############################################################################3

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from .models import Owner


class OwnerView(APIView):
    def get(self, request: Request, pk=None):
        if pk:
            owner = Owner.objects.filter(pk=pk).values().first()

            if not owner:
                raise NotFound(detail=f"{pk} - Owner topilmadi!")
            return Response(owner)

        owners = Owner.objects.values()
        return Response(owners)

    def post(self, request: Request):
        body = request.data
        Owner.objects.create(**body)
        return Response({"message": "Owner saqlandi!"})

    def put(self, request: Request, pk):
        owner = Owner.objects.filter(pk=pk).first()

        if not owner:
            raise NotFound(detail=f"{pk} - Owner topilmadi!")

        body = request.data

        owner.first_name = body.get("first_name", owner.first_name)
        owner.last_name = body.get("last_name", owner.last_name)
        owner.age = body.get("age", owner.age)
        owner.email = body.get("email", owner.email)
        owner.save()

        return Response({"message": "Owner yangilandi!"})

    def patch(self, request: Request, pk):
        owner = Owner.objects.filter(pk=pk).first()

        if not owner:
            raise NotFound(detail=f"{pk} - Owner topilmadi!")

        body = request.data

        owner.first_name = body.get("first_name", owner.first_name)
        owner.last_name = body.get("last_name", owner.last_name)
        owner.age = body.get("age", owner.age)
        owner.email = body.get("email", owner.email)
        owner.save()

        return Response({"message": "Owner yangilandi!"})

    def delete(self, request: Request, pk):
        owner = Owner.objects.filter(pk=pk).first()

        if not owner:
            raise NotFound(detail=f"{pk} - Owner topilmadi!")

        owner.delete()
        return Response({"message": "Owner o'chirildi!"})