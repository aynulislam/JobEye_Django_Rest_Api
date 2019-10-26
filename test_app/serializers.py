from rest_framework import serializers
from .models import JeQuestion,JeTest,JeTestDetails
class JeQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JeQuestion
        fields = "__all__"


class JeTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = JeTest
        fields = "__all__"


class JeTestDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JeTestDetails
        fields = "__all__"


