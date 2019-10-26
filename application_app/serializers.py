from rest_framework import serializers
from .models import JeJobApplication,JeWorkStatus
class JeJobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JeJobApplication
        fields = "__all__"


class JeWorkStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = JeWorkStatus
        fields = "__all__"





