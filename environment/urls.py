

from django.urls import path
from .views import EnvironmentListView, EnvironmentDetailView


urlpatterns = [
    path("", EnvironmentListView.as_view()),
    path('<str:pk>/', EnvironmentDetailView.as_view())
]
