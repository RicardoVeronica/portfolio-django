from rest_framework import serializers
from portfolio.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    """
    Transform Project model fields into JSON for API
    """
    class Meta:
        model = Project
        fields = '__all__'
