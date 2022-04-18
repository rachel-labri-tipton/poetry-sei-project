from django.urls import path

from .views import WhaleDetailView, WhaleView


urlpatterns = [
    path('', WhaleView.as_view()),
    path('<str:pk>/', WhaleDetailView.as_view())
]
