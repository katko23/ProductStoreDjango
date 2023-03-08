from rest_framework import serializers
from .models import Product, ProductImage, ProductCharacteristic


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image']


class ProductCharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCharacteristic
        fields = ['id', 'name', 'value']


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    characteristics = ProductCharacteristicSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'date_added', 'user', 'images', 'characteristics']
