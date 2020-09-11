from django.urls import path
from .views import ProjectApiView, ProjectDetailView

urlpatterns = [
    path('', ProjectApiView.as_view()),
    path('project/<int:pk>/', ProjectDetailView.as_view()),
]
