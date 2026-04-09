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