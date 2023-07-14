from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Menu,Booking,MenuItem,category

class menuserialzer(serializers.ModelSerializer):
    class meta:
        model=Menu
        fields='__all__'
    
class bookingserializer(serializers.ModelSerializer):
        class meta:
            model=Booking
            fields='__all__'
            
class CategorySerializer (serializers.ModelSerializer):
     class Meta:
         model = category
         fields = ['id','title']

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['title','price','featured','Category']