from django.urls import path
from .views import ProjectApiView

urlpatterns = [
    path('', ProjectApiView.as_view()),
]
