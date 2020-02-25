from django.shortcuts import render

# Create your views here.
from rest_framework import serializers
from rest_framework.response import  Response
from  rest_framework.views import  APIView
from apiapp.serializers import NameSerializer

class TestAPIview(APIView):
    def get(self,request,*args,**kwargs):
        colours = ['red', 'green', 'blue', 'violet']
        msg = {'msg': 'thesee are the colours', 'colours': colours}
        return Response(msg)
    def post(self,request,*args,**kwargs):
        serializer=NameSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            msg='hello {} welcome'.format(name)
            return Response({'msg':msg})
        else:
            return Response(serializer.errrors)
    def put(self,request,*args,**kwargs):
        return Response({'msg':'this is from put method of APIView'})
    def patch(self,request,*args,**kwargs):
        return Response({'msg':'this is from patch method of APIView'})

    def delete(self, request, *args, **kwargs):
        return Response({'msg': 'this is from delete method of APIView'})

##########################################################################################


from rest_framework.viewsets import  ViewSet

class TestViewSet(ViewSet):
    def  list(self, request):
        colours = ['red', 'green', 'blue', 'violet']
        msg = {'msg': 'thesee are the colours', 'colours': colours}
        return Response(msg)

    def create(self, request):
        serializer = NameSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            msg = 'hello {} welcome'.format(name)
            return Response({'msg': msg})
        else:
            return Response(serializer.errrors)

    def retrieve(self, request, pk=None):
        return Response({'msg': 'this is from retrieve method of Viewset'})

    def update(self, request , pk=None):
        return Response({'msg': 'this is from put method of APIView'})

    def partial_update(self, request ,pk=None):
        return Response({'msg': 'this is from patch method of APIView'})

    def destroy(self, request, pk=None):
        return Response({'msg': 'this is from delete method of APIView'})



