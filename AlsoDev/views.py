from rest_framework import generics
from .models import Product, ProductImage, ProductCharacteristic
from .serializers import ProductSerializer, ProductImageSerializer, ProductCharacteristicSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductImageListCreateView(generics.ListCreateAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

class ProductImageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

class ProductCharacteristicListCreateView(generics.ListCreateAPIView):
    queryset = ProductCharacteristic.objects.all()
    serializer_class = ProductCharacteristicSerializer

class ProductCharacteristicRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductCharacteristic.objects.all()
    serializer_class = ProductCharacteristicSerializer
