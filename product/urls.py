from django.urls import path, include
from rest_framework import routers
from .views import base, form, main_get
from .api import UserViewSet, GroupViewSet

# API
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    # API
    path('api/v1', include(router.urls)),

    # VIEW
    path ('', base, name='base'),
    path ('add', form, name='form'),
    path ('product/<int:main_id>', main_get, name='main_id')
]