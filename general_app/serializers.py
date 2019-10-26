from rest_framework import serializers
from .models import JeCategory,JeSubCategory,JeJobType,JeDurationUnitType,JeRateUnitType,JeBuyer,JeSkill,JeSkillType,JeWorkStatus

class JeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JeCategory
        fields = "__all__"


class JeSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JeSubCategory
        fields = "__all__"


class JeJobTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JeJobType
        fields = "__all__"


class JeDurationUnitTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JeDurationUnitType
        fields = "__all__"

class JeRateUnitTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JeRateUnitType
        fields = "__all__"

class JeBuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = JeBuyer
        fields = "__all__"



class JeSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = JeSkill
        fields = "__all__"

class JeSkillTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JeSkillType
        fields = "__all__"

class JeWorkStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = JeWorkStatus
        fields = "__all__"
