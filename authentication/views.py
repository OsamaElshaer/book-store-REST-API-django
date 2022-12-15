from authentication.serializers import Userserializer
from shop.models import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class RegisterView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]   
    queryset = User.objects.all()
    serializer_class = Userserializer

    def post(self,request):
        serializers = Userserializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'error':False})
        return Response({'error':True})    
