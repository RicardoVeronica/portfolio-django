from rest_framework import generics
from portfolio.models import Project
from .serializers import ProjectSerializer


class ProjectApiView(generics.ListAPIView):
    """
    GET: list all projects in portfolio
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
