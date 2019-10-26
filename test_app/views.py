from django.shortcuts import render

# Create your views here.


from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from rest_framework import generics
from .models import  JeTest,JeQuestion,JeTestDetails

from .serializers  import JeTestSerializer,JeTestDetailsSerializer,JeQuestionSerializer




class JeTestAPIView(generics.ListCreateAPIView):
    queryset = JeTest.objects.all()
    serializer_class = JeTestSerializer

class JeTestDetailsAPIView(generics.ListCreateAPIView):
    queryset = JeTestDetails.objects.all()
    serializer_class = JeTestDetailsSerializer

class JeQuestionAPIView(generics.ListCreateAPIView):
    queryset = JeQuestion.objects.all()
    serializer_class = JeQuestionSerializer

#Test app Api Create


from general_app.serializers import JeCategorySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class JeQuestionDetail(APIView):
    """
    Retrieve, update or delete a  instance.
    """
    def get_object(self, pk):
        try:
            return JeQuestion.objects.get(pk=pk)
        except JeQuestion.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        jequestion = self.get_object(pk)
        serializer = JeQuestionSerializer(jequestion)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        jequestion = self.get_object(pk)
        serializer = JeQuestionSerializer(jequestion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        jequestion = self.get_object(pk)
        jequestion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class JeQuestionList(APIView):
    """
    List all , or create a new .
    """
    def get(self, request, format=None):
        jequestion = JeQuestion.objects.all()
        serializer = JeQuestionSerializer(jequestion, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = JeQuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Je Test Api

class JeTestDetailsDetail(APIView):
    """
    Retrieve, update or delete a  instance.
    """
    def get_object(self, pk):
        try:
            return JeTestDetails.objects.get(pk=pk)
        except JeTestDetails.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        jetestdetails = self.get_object(pk)
        serializer = JeTestDetailsSerializer(jetestdetails)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        jetestdetails = self.get_object(pk)
        serializer = JeTestDetailsSerializer(jetestdetails, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        jetestdetails = self.get_object(pk)
        jetestdetails.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class JeTestDetailsList(APIView):
    """
    List all , or create a new .
    """
    def get(self, request, format=None):
        jetestdetails = JeTestDetails.objects.all()
        serializer = JeTestDetailsSerializer(jetestdetails, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = JeTestDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Je Test Api

class JeTestDetail(APIView):
    """
    Retrieve, update or delete a  instance.
    """
    def get_object(self, pk):
        try:
            return JeTest.objects.get(pk=pk)
        except JeTest.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        jetest = self.get_object(pk)
        serializer = JeTestSerializer(jetest)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        jetest = self.get_object(pk)
        serializer = JeTestSerializer(jetest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        jetest = self.get_object(pk)
        jetest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class JeTestList(APIView):
    """
    List all , or create a new .
    """
    def get(self, request, format=None):
        jetest = JeTest.objects.all()
        serializer = JeTestSerializer(jetest, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = JeTestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

