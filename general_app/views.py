


from django.shortcuts import render
from rest_framework import generics
from .models import JeCategory,JeSubCategory,JeJobType,JeDurationUnitType,JeRateUnitType,JeSkill,JeSkillType,JeWorkStatus

from .serializers import JeCategorySerializer,JeSubCategorySerializer,JeJobTypeSerializer,JeDurationUnitTypeSerializer,JeRateUnitTypeSerializer,JeSkillSerializer,JeSkillTypeSerializer,JeWorkStatusSerializer




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

class JeSkillAPIView(generics.ListCreateAPIView):
    queryset = JeSkill.objects.all()
    serializer_class = JeSkillSerializer

class  JeSkillTypeAPIView(generics.ListCreateAPIView):
    queryset = JeSkillType.objects.all()
    serializer_class = JeSkillTypeSerializer

class  JeWorkStatusAPIView(generics.ListCreateAPIView):
    queryset = JeWorkStatus.objects.all()
    serializer_class = JeWorkStatusSerializer




from .models import JeCategory
from general_app.serializers import JeCategorySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



#JeCategory API Crteate

class JeCategoryDetail(APIView):
    """
    Retrieve, update or delete a  instance.
    """
    def get_object(self, pk):
        try:
            return JeCategory.objects.get(pk=pk)
        except JeCategory.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        jecategory = self.get_object(pk)
        serializer = JeCategorySerializer(jecategory)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        jecategory = self.get_object(pk)
        serializer = JeCategorySerializer(jecategory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        jecategory = self.get_object(pk)
        jecategory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class JeCategoryList(APIView):
    """
    List all snippets, or create a new .
    """
    def get(self, request, format=None):
        jecategory = JeCategory.objects.all()
        serializer = JeCategorySerializer(jecategory, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = JeCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#JeSubCategory API Crteate

class JeSubCategoryDetail(APIView):
    """
    Retrieve, update or delete a  instance.
    """
    def get_object(self, pk):
        try:
            return JeSubCategory.objects.get(pk=pk)
        except JeSubCategory.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        jesubcategory = self.get_object(pk)
        serializer = JeSubCategorySerializer(jesubcategory)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        jesubcategory = self.get_object(pk)
        serializer = JeCategorySerializer(jesubcategory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        jesubcategory = self.get_object(pk)
        jesubcategory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class JeSubCategoryList(APIView):
    """
    List all snippets, or create a new .
    """
    def get(self, request, format=None):
        jesubcategory = JeSubCategory.objects.all()
        serializer = JeSubCategorySerializer(jesubcategory, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = JeCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#JeJobType API Crteate


class JeJobTypeDetail(APIView):
    """
    Retrieve, update or delete a  instance.
    """
    def get_object(self, pk):
        try:
            return JeJobType.objects.get(pk=pk)
        except JeJobType.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        jejobtype = self.get_object(pk)
        serializer = JeJobTypeSerializer(jejobtype)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        jejobtype = self.get_object(pk)
        serializer = JeJobTypeSerializer(jejobtype, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        jejobtype = self.get_object(pk)
        jejobtype.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class JeJobTypeList(APIView):
    """
    List all , or create a new .
    """
    def get(self, request, format=None):
        jejobtype = JeJobType.objects.all()
        serializer = JeJobTypeSerializer(jejobtype, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = JeJobTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#JeRateType API Crteate


class JeRateUnitTypeDetail(APIView):
    """
    Retrieve, update or delete a  instance.
    """
    def get_object(self, pk):
        try:
            return JeRateUnitType.objects.get(pk=pk)
        except JeRateUnitType.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        jerateunittype = self.get_object(pk)
        serializer = JeRateUnitTypeSerializer(jerateunittype)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        jerateunittype = self.get_object(pk)
        serializer = JeRateUnitTypeSerializer(jerateunittype, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        jerateunittype = self.get_object(pk)
        jerateunittype.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class JeRateUnitTypeList(APIView):
    """
    List all , or create a new .
    """
    def get(self, request, format=None):
        jerateunittype = JeRateUnitType.objects.all()
        serializer = JeRateUnitTypeSerializer(jerateunittype, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = JeRateUnitTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#JeDurationUnitType API Crteate


class JeDurationUnitTypeDetail(APIView):
    """
    Retrieve, update or delete a  instance.
    """
    def get_object(self, pk):
        try:
            return JeDurationUnitType.objects.get(pk=pk)
        except JeDurationUnitType.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        jedurationunittype = self.get_object(pk)
        serializer = JeDurationUnitTypeSerializer(jedurationunittype)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        jedurationunittype = self.get_object(pk)
        serializer = JeDurationUnitTypeSerializer(jedurationunittype, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        jedurationunittype = self.get_object(pk)
        jedurationunittype.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class JeDurationUnitTypeList(APIView):
    """
    List all , or create a new .
    """
    def get(self, request, format=None):
        jedurationunittype = JeDurationUnitType.objects.all()
        serializer = JeDurationUnitTypeSerializer(jedurationunittype, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = JeDurationUnitTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#JeSkillType API Crteate


class JeSkillTypeDetail(APIView):
    """
    Retrieve, update or delete a  instance.
    """
    def get_object(self, pk):
        try:
            return JeSkillType.objects.get(pk=pk)
        except JeSkillType.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        jeskilltype = self.get_object(pk)
        serializer = JeSkillTypeSerializer(jeskilltype)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        jeskilltype = self.get_object(pk)
        serializer = JeSkillTypeSerializer(jeskilltype, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        jeskilltype = self.get_object(pk)
        jeskilltype.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class JeSkillTypeList(APIView):
    """
    List all , or create a new .
    """
    def get(self, request, format=None):
        jeskilltype = JeSkillType.objects.all()
        serializer = JeSkillTypeSerializer(jeskilltype, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = JeSkillTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#JeWorkStatus API Crteate


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
        jeworkstatus = self.get_object(pk)
        serializer = JeWorkStatusSerializer(jeworkstatus)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        jeworkstatus = self.get_object(pk)
        serializer = JeWorkStatusSerializer(jeworkstatus, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        jeworkstatus = self.get_object(pk)
        jeworkstatus.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class JeWorkStatusList(APIView):
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

