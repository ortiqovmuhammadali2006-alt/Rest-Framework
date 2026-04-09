from django.urls import path
from .views import CarView

urlpatterns = [
    path('cars/', CarView.as_view()),
    path('cars/<int:pk>/', CarView.as_view()),
]