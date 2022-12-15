from rest_framework import serializers
from shop.models import *



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__" 


class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"


class CartBookSerializers(serializers.ModelSerializer):
    class Meta:
        model = CartBook
        fields = "__all__"


class OrdersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
