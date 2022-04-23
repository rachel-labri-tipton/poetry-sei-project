from django.urls import path
from .views import WhaleDetailView, WhaleList


urlpatterns = [
    path('', WhaleList.as_view()),
    path('<int:pk>/', WhaleDetailView.as_view()),
]
