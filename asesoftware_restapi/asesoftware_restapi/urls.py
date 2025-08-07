from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from orders.api_functions import getProviders, createOrder


urlpatterns = [
    # Endpoint para obtener proveedores
    path('api/sap/providers/', getProviders), 
    # Endpoint para crear ordenes
    path('api/orders/', createOrder),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]



