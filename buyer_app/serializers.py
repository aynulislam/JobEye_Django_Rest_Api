from rest_framework import serializers
from .models import ScUser,JeBuyer


class JeBuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = JeBuyer
        fields = "__all__"


class ScUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScUser
        fields = "__all__"

