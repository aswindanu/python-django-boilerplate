from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['url', 'product_id', 'product_name', 'quantity', 'price', 'description']

class ProductSerializerAPIView(serializers.Serializer):
    product_id = serializers.CharField()
    product_name = serializers.CharField()
    description = serializers.CharField()
    images = serializers.ImageField()
    price = serializers.IntegerField()
    quantity = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    version = serializers.IntegerField()