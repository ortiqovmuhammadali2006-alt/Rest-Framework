from rest_framework import serializers

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
        
    


