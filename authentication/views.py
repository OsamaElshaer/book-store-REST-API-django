from authentication.serializers import Userserializer
from core.models import *
from rest_framework import generics
from rest_framework.response import Response


# Create your views here.

class RegisterView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer

    def post(self,request):
        serializers = Userserializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'error':False})
        return Response({'error':True})    
