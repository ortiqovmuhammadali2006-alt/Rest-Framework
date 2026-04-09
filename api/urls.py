from django.urls import path
from .views import CarView, OwnerView

urlpatterns = [
    path('cars/', CarView.as_view()),
    path('cars/<int:pk>/', CarView.as_view()),
    
    path('owners/', OwnerView.as_view()),
    path('owners/<int:pk>/', OwnerView.as_view()),
]