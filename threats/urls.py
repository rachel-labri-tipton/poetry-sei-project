from django.urls import path
from .views import ThreatDetailView, ThreatsView


urlpatterns = [
    path("", ThreatsView.as_view()),
    path('<str:pk>/', ThreatDetailView.as_view())
]
