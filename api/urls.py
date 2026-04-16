from django.urls import path
from .views import (
    CarListCreateView,
    CarRetrieveUpdateDestroyView,
    OwnerRetrieveUpdateDestroyView,
    RegisterView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    
)

urlpatterns = [
    path("cars/", CarListCreateView.as_view(), name="car_create"),
    path("cars/<int:pk>/", CarRetrieveUpdateDestroyView.as_view(), name="car_detail"),
    path("owners/", CarListCreateView.as_view(), name="car_create"),
    path(
        "owners/<int:pk>/",
        OwnerRetrieveUpdateDestroyView.as_view(),
        name="owner_detail",
    ),
    path('register/', RegisterView.as_view(), name='register'),
    
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
