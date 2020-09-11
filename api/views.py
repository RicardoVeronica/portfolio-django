from .permissions import IsAuthorOrReadOnly
from .serializers import ProjectSerializer
from rest_framework import generics
from portfolio.models import Project


class ProjectApiView(generics.ListCreateAPIView):
    """
    GET: list all projects in portfolio
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: detail item in list projects
    """
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
