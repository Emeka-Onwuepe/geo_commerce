from rest_framework import serializers

from Product.models import (Product,Category,Size,Product_Type)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # depth = 1
        exclude = ('image',)
        
class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        # depth = 1
        fields = '__all__'
        
class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Type
        # depth = 1
        fields = '__all__'

        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # depth = 1
        exclude = ('date','image','publish')