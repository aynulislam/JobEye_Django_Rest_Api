from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from rest_framework import generics
from .models import  JeWorker,JeWorkerPortfolio,JeWorkerSkill,JeWorkerCertification,JeCertification

from .serializers  import JeWorkerSerializer,JeWorkerPortfolioSerializer,JeWorkerSkillSerializer,JeWorkerCertificationSerializer,JeCertificationSerializer




class JeWorkerAPIView(generics.ListCreateAPIView):
    queryset = JeWorker.objects.all()
    serializer_class = JeWorkerSerializer

class JeWorkerPortfolioAPIView(generics.ListCreateAPIView):
    queryset = JeWorkerPortfolio.objects.all()
    serializer_class = JeWorkerPortfolioSerializer

class JeWorkerSkillAPIView(generics.ListCreateAPIView):
    queryset = JeWorkerSkill.objects.all()
    serializer_class = JeWorkerSkillSerializer

class JeWorkerCertificationAPIView(generics.ListCreateAPIView):
    queryset = JeWorkerCertification.objects.all()
    serializer_class = JeWorkerCertificationSerializer


class JeCertificationAPIView(generics.ListCreateAPIView):
    queryset = JeCertification.objects.all()
    serializer_class = JeCertificationSerializer

#Je Worker Api


from general_app.serializers import JeCategorySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class JeWorkerDetail(APIView):
    """
    Retrieve, update or delete a  instance.
    """
    def get_object(self, pk):
        try:
            return JeWorker.objects.get(pk=pk)
        except JeWorker.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        jeworker = self.get_object(pk)
        serializer = JeWorkerSerializer(jeworker)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        jeworker = self.get_object(pk)
        serializer = JeWorkerSerializer(jeworker, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        jeworker = self.get_object(pk)
        jeworker.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class JeWorkerList(APIView):
    """
    List all , or create a new .
    """
    def get(self, request, format=None):
        jeworker = JeWorker.objects.all()
        serializer = JeWorkerSerializer(jeworker, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = JeWorkerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Je Worker Skill Api Create

class JeWorkerSkillDetail(APIView):
    """
    Retrieve, update or delete a  instance.
    """
    def get_object(self, pk):
        try:
            return JeWorkerSkill.objects.get(pk=pk)
        except JeWorkerSkill.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        jeworkerskill = self.get_object(pk)
        serializer = JeWorkerSerializer(jeworkerskill)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        jeworkerskill = self.get_object(pk)
        serializer = JeWorkerSerializer(jeworkerskill, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        jeworkerskill = self.get_object(pk)
        jeworkerskill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class JeWorkerSkillList(APIView):
    """
    List all , or create a new .
    """
    def get(self, request, format=None):
        jeworkerskill = JeWorker.objects.all()
        serializer = JeWorkerSerializer(jeworkerskill, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = JeWorkerSkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Je Worker Portfolio Api

class JeWorkerPortfolioDetail(APIView):
    """
    Retrieve, update or delete a  instance.
    """
    def get_object(self, pk):
        try:
            return JeWorkerPortfolio.objects.get(pk=pk)
        except JeWorkerPortfolio.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        jeworkerportfolio = self.get_object(pk)
        serializer = JeWorkerPortfolioSerializer(jeworkerportfolio)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        jeworkerportfolio = self.get_object(pk)
        serializer = JeWorkerPortfolioSerializer(jeworkerportfolio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        jeworkerportfolio = self.get_object(pk)
        jeworkerportfolio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class JeWorkerPortfolioList(APIView):
    """
    List all , or create a new .
    """
    def get(self, request, format=None):
        jeworkerportfolio = JeWorkerPortfolio.objects.all()
        serializer = JeWorkerPortfolioSerializer(jeworkerportfolio, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = JeWorkerPortfolioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Je Worker Certification

class JeWorkerCertificationDetail(APIView):
    """
    Retrieve, update or delete a  instance.
    """
    def get_object(self, pk):
        try:
            return JeWorkerCertification.objects.get(pk=pk)
        except JeWorkerCertification.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        jeworkercertification = self.get_object(pk)
        serializer = JeWorkerCertificationSerializer(jeworkercertification)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        jeworkercertification = self.get_object(pk)
        serializer = JeWorkerCertificationSerializer(jeworkercertification, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        jeworkercertification = self.get_object(pk)
        jeworkercertification.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class JeWorkerCertificationList(APIView):
    """
    List all , or create a new .
    """
    def get(self, request, format=None):
        jeworkercertification = JeWorker.objects.all()
        serializer = JeWorkerCertificationSerializer(jeworkercertification, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = JeWorkerCertificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Je Certification Api Create

class JeCertificationDetail(APIView):
    """
    Retrieve, update or delete a  instance.
    """
    def get_object(self, pk):
        try:
            return JeCertification.objects.get(pk=pk)
        except JeCertification.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        jecertification = self.get_object(pk)
        serializer = JeCertificationSerializer(jecertification)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        jecertification = self.get_object(pk)
        serializer = JeCertificationSerializer(jecertification, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        jecertification = self.get_object(pk)
        jecertification.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class JeCertificationList(APIView):
    """
    List all , or create a new .
    """
    def get(self, request, format=None):
        jecertification = JeCertification.objects.all()
        serializer = JeCertificationSerializer(jecertification, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = JeCertificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


