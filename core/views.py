from django.shortcuts import render


def home(request):
    """
    home view
    """
    template = 'core/home.html'
    return render(request, template)
