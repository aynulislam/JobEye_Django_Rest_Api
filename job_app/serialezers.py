from rest_framework import serializers
from .models import JeCategory,JeSubCategory,JeJobType,JeDurationUnitType,JeRateUnitType,JeBuyer,JeJob,JeJobSkill,JeJobAttachment

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

class JeJobSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = JeJobSkill
        fields = "__all__"

class JeJobAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = JeJobAttachment
        fields = "__all__"



class JeJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = JeJob
        fields = "__all__"