from rest_framework import serializers
from shop.models import *
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token



User = get_user_model()

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','first_name','last_name','email',)
        # extra_kwargs = {'password': {"write_only":True,'required':True}}
    
    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


