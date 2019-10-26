# Create your views here.

from django.shortcuts import render
from rest_framework import generics
from .models import  JeJobApplication,JeWorkStatus

from .serializers  import JeJobApplicationSerializer,JeWorkStatusSerializer


class JeJobApplicationAPIView(generics.ListCreateAPIView):
    queryset = JeJobApplication.objects.all()
    serializer_class = JeJobApplicationSerializer

class JeWorkStatusAPIView(generics.ListCreateAPIView):
    queryset = JeWorkStatus.objects.all()
    serializer_class = JeWorkStatusSerializer




from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


#Application Api Create

class JeJobApplicationDetail(APIView):
    """
    Retrieve, update or delete a  instance.
    """
    def get_object(self, pk):
        try:
            return JeJobApplication.objects.get(pk=pk)
        except JeWorkStatus.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        jejobapplication = self.get_object(pk)
        serializer = JeJobApplicationSerializer(jejobapplication)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        jejobapplication = self.get_object(pk)
        serializer = JeJobApplicationSerializer(jejobapplication, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        jejobapplication = self.get_object(pk)
        jejobapplication.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class JeJobApplicationList(APIView):
    """
    List all , or create a new .
    """
    def get(self, request, format=None):
        jejobapplication = JeJobApplication.objects.all()
        serializer = JeJobApplicationSerializer(jejobapplication, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = JeJobApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Je Job Work Status Api create

class JeWorkStatusDetail(APIView):
    """
    Retrieve, update or delete a  instance.
    """
    def get_object(self, pk):
        try:
            return JeWorkStatus.objects.get(pk=pk)
        except JeWorkStatus.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        jejobworkstatus = self.get_object(pk)
        serializer = JeWorkStatusSerializer(jejobworkstatus)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        jejobworkstatus = self.get_object(pk)
        serializer = JeWorkStatusSerializer(jejobworkstatus, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        jejobworkstatus = self.get_object(pk)
        jejobworkstatus.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class JeJobWorkStatusList(APIView):
    """
    List all , or create a new .
    """
    def get(self, request, format=None):
        jeworkstatus = JeWorkStatus.objects.all()
        serializer = JeWorkStatusSerializer(jeworkstatus, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = JeWorkStatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

