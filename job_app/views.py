# Create your views here.

from django.shortcuts import render
from rest_framework import generics
from general_app.models import JeCategory,JeSubCategory,JeJobType,JeDurationUnitType,JeRateUnitType
from job_app.models import JeJobSkill,JeJobAttachment,JeBuyer,JeJob
from general_app.serializers import JeCategorySerializer,JeSubCategorySerializer,JeJobTypeSerializer,JeDurationUnitTypeSerializer,JeRateUnitTypeSerializer,JeSkillSerializer,JeSkillTypeSerializer,JeWorkStatusSerializer
from job_app.serialezers import JeJobSerializer,JeJobSkillSerializer,JeJobAttachmentSerializer,JeBuyerSerializer


class JeCategoryAPIView(generics.ListCreateAPIView):
    queryset = JeCategory.objects.all()
    serializer_class = JeCategorySerializer

class JeSubCategoryAPIView(generics.ListCreateAPIView):
    queryset = JeSubCategory.objects.all()
    serializer_class = JeSubCategorySerializer

class JeJobTypeAPIView(generics.ListCreateAPIView):
    queryset = JeJobType.objects.all()
    serializer_class = JeJobTypeSerializer

class JeDurationUnitTypeAPIView(generics.ListCreateAPIView):
    queryset = JeDurationUnitType.objects.all()
    serializer_class = JeDurationUnitTypeSerializer

class JeRateUnitTypeAPIView(generics.ListCreateAPIView):
    queryset = JeRateUnitType.objects.all()
    serializer_class = JeRateUnitTypeSerializer

class JeBuyerAPIView(generics.ListCreateAPIView):
    queryset = JeBuyer.objects.all()
    serializer_class = JeBuyerSerializer

class  JeJobAPIView(generics.ListCreateAPIView):
    queryset = JeJob.objects.all()
    serializer_class = JeJobSerializer

class JeJobSkillAPIView(generics.ListCreateAPIView):
    queryset = JeJobSkill.objects.all()
    serializer_class = JeJobSkillSerializer

class  JeJobAttachmentAPIView(generics.ListCreateAPIView):
    queryset = JeJobAttachment.objects.all()
    serializer_class = JeJobAttachmentSerializer

from .models import JeJob
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status




#JeJob API Crteate


class JeJobDetail(APIView):
    """
    Retrieve, update or delete a  instance.
    """
    def get_object(self, pk):
        try:
            return JeJob.objects.get(pk=pk)
        except JeJob.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        jejob = self.get_object(pk)
        serializer = JeJobSerializer(jejob)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        jejob = self.get_object(pk)
        serializer = JeJobSerializer(jejob, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        jejob = self.get_object(pk)
        jejob.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class JeJobList(APIView):
    """
    List all , or create a new .
    """
    def get(self, request, format=None):
        jejob = JeJob.objects.all()
        serializer = JeJobSerializer(jejob, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = JeJobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#JeJobSkill API Crteate


class JeJobSkillDetail(APIView):
    """
    Retrieve, update or delete a  instance.
    """
    def get_object(self, pk):
        try:
            return JeJobSkill.objects.get(pk=pk)
        except JeJobSkill.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        jejobskill = self.get_object(pk)
        serializer = JeJobSkillSerializer(jejobskill)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        jejobskill = self.get_object(pk)
        serializer = JeJobSkillSerializer(jejobskill, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        jejobskill = self.get_object(pk)
        jejobskill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class JeJobSkillList(APIView):
    """
    List all , or create a new .
    """
    def get(self, request, format=None):
        jejobskill = JeJobSkill.objects.all()
        serializer = JeJobSkillSerializer(jejobskill, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = JeJobSkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#JeJob Attachment Api

class JeJobAttachmentDetail(APIView):
    """
    Retrieve, update or delete a  instance.
    """
    def get_object(self, pk):
        try:
            return JeJobAttachment.objects.get(pk=pk)
        except JeJobAttachment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        jejobattachment = self.get_object(pk)
        serializer = JeJobAttachmentSerializer(jejobattachment)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        jejobattachment = self.get_object(pk)
        serializer = JeJobAttachmentSerializer(jejobattachment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        jejobattachment = self.get_object(pk)
        jejobattachment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class JeJobAttachmentList(APIView):
    """
    List all , or create a new .
    """
    def get(self, request, format=None):
        jejobattachment = JeJobAttachment.objects.all()
        serializer = JeJobSkillSerializer(jejobattachment, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = JeJobAttachmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

