from rest_framework import serializers
from.models import *

class BookSerializer(serializers.ModelSerializer):
    is_available = serializers.SerializerMethodField()
   

    class Meta:
        model = Book
        fields = ('id', 'name', 'author', 'qty', 'is_available')

    def get_is_available(self, instance):
        if instance.is_available:
            return 'stock available'
        else:
            return 'Out of stock'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=[
        'id',
        'username',
        'mobile',
        'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = '__all__'
       