

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from .models import  ScUser, JeBuyer

from .serializers  import ScUserSerializer,JeBuyerSerializer



class JeBuyerAPIView(generics.ListCreateAPIView):
    queryset = JeBuyer.objects.all()
    serializer_class = JeBuyerSerializer

class ScUserAPIView(generics.ListCreateAPIView):
    queryset = ScUser.objects.all()
    serializer_class = ScUserSerializer



from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


#Je Buyer Api create
class JeBuyerDetail(APIView):
    """
    Retrieve, update or delete a  instance.
    """
    def get_object(self, pk):
        try:
            return JeBuyer.objects.get(pk=pk)
        except JeBuyer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        jebuyer = self.get_object(pk)
        serializer = JeBuyerSerializer(jebuyer)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        jebuyer = self.get_object(pk)
        serializer = JeBuyerSerializer(jebuyer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        jebuyer = self.get_object(pk)
        jebuyer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class JeBuyerList(APIView):
    """
    List all , or create a new .
    """
    def get(self, request, format=None):
        jebuyer = JeBuyer.objects.all()
        serializer = JeBuyerSerializer(jebuyer, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = JeBuyerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Je User Api create

#Je Buyer Api create
class ScUserDetail(APIView):
    """
    Retrieve, update or delete a  instance.
    """
    def get_object(self, pk):
        try:
            return ScUser.objects.get(pk=pk)
        except ScUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        scuser = self.get_object(pk)
        serializer = ScUserSerializer(scuser)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        scuser = self.get_object(pk)
        serializer = ScUserSerializer(scuser, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        scuser = self.get_object(pk)
        scuser.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ScUserList(APIView):
    """
    List all , or create a new .
    """
    def get(self, request, format=None):
        scuser = ScUser.objects.all()
        serializer = ScUserSerializer(scuser, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ScUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

