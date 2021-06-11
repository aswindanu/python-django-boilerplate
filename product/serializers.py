# from django.contrib.auth.models import User
from rest_framework import serializers
from account.models import User
from .models import Product


class ProductSerializerGeneric(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "description", "images", "price", "quantity"]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['url', 'id', 'name', 'quantity', 'price', 'description']


class ProductSerializerAPIView(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    description = serializers.CharField()
    images = serializers.ImageField()
    price = serializers.IntegerField()
    quantity = serializers.IntegerField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.images = validated_data.get('images', instance.images)
        instance.price = validated_data.get('price', instance.price)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()

        return instance
