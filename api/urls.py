from django.urls import path
from .views import CarListView, CarListCreateView, CarRetrieveUpdateDestroyView, OwnerListView


urlpatterns = [
    path('cars/', CarListView.as_view(), name='cars'),   
    path('cars/create', CarListCreateView.as_view(), name='car_create'),
    
    path('owners/', OwnerListView.as_view(), name='owners'),   
    path('owners/create', CarListCreateView.as_view(), name='car_create'),
    
    path('cars/<int:pk>/', CarRetrieveUpdateDestroyView.as_view(), name='car_detail'),



    
]