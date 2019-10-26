from rest_framework import serializers
from .models import JeWorker,JeWorkerPortfolio,JeWorkerSkill,JeWorkerCertification,JeCertification
class JeWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = JeWorker
        fields = "__all__"


class JeWorkerPortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = JeWorkerPortfolio
        fields = "__all__"


class JeWorkerSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = JeWorkerSkill
        fields = "__all__"


class JeWorkerCertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JeWorkerCertification
        fields = "__all__"

class JeCertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JeCertification
        fields = "__all__"
