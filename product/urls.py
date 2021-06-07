from django.urls import path, include
from rest_framework import routers
from .views import base, form, clear_cache, product_get
from .api import UserViewSet, ProductViewSet

# API
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    # API
    path('api/v1/', include(router.urls)),

    # VIEW
    path ('', base, name='base'),
    path ('clear', clear_cache, name='logout'),
    path ('add', form, name='form'),
    path ('product/<int:product_id>', product_get, name='product_id')
]