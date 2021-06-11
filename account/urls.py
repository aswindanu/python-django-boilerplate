from rest_framework.authtoken import views
from django.urls import path, include
from rest_framework import routers


urlpatterns = [
    # API
    path('api/v1/api-token-auth/', views.obtain_auth_token)
]