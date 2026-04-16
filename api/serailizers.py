from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Car, Owner


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"
        read_only_fields = ("id",)

    def validate_name(self, value):
        if not value.istitle():
            raise serializers.ValidationError("Nomi bosh harf katta harf bo'lish kerak")

        return value

    def validate_brand(self, value):
        if not value.istitle():
            raise serializers.ValidationError(
                "Brand bosh harf katta harf bo'lish kerak"
            )

        elif not value.isalpha():
            raise serializers.ValidationError(
                "Brand faqat harfdan tashkil topgan bo'lishi kerak"
            )

        return value

    def validate_color(self, value):
        if not value.istitle():
            raise serializers.ValidationError(
                "Color bosh harf katta harf bo'lish kerak"
            )

        return value

    def validate_year(self, value):
        if not value > 2010:
            raise serializers.ValidationError(
                "Avtomobilni yili 2010 dan katta bolishi kerak"
            )

        return value


User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(min_length=8, max_length=126, write_only=True)
    password2 = serializers.CharField(min_length=8, max_length=126, write_only=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def validate(self, attrs):
        password1 = attrs.get("password1")
        password2 = attrs.get("password2")

        if password1 != password2:
            raise serializers.ValidationError(
                {"password1": "Parollar bir-biriga mos emas"}
            )

        return attrs

    def create(self, validated_data):
        validated_data.pop("password2")
        password = validated_data.pop("password1")
        return User.objects.create_user(password=password, **validated_data)


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = "__all__"
        read_only_fields = ("id",)

    def validate_first_name(self, value):
        if not value.istitle():
            raise serializers.ValidationError(
                "Ismni bosh harf katta harf bo'lish kerak"
            )

        elif not value.isalpha():
            raise serializers.ValidationError(
                "Ismni faqat harfdan tashkil topgan bo'lishi kerak"
            )

        return value

    def validate_last_name(self, value):
        if not value.istitle():
            raise serializers.ValidationError(
                "Familiya bosh harf katta harf bo'lish kerak"
            )

        elif not value.isalpha():
            raise serializers.ValidationError(
                "Familiya faqat harfdan tashkil topgan bo'lishi kerak"
            )

        return value

    def validate(self, value):
        if not value > 20:
            raise serializers.ValidationError("Sizga avtomobil haydash huquqi yo'q")

        return value


class OwnerAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        exclude = ("age",)
        read_only_fields = ("id",)
