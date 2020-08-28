from django.shortcuts import render
from .models import Project


def portfolio(request):
    """
    portfolio view
    """
    projects = Project.objects.all()
    template = 'portfolio/portfolio.html'
    return render(request, template, {'projects': projects})
