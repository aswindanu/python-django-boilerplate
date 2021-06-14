from django.urls import path, include
from rest_framework import routers
from product.views import base, form, clear_cache, product_get
from product.api import (
    ProductListGeneric,
    ProductDetailGeneric,
    ProductListMixins,
    ProductDetailMixins,
    UserViewSet,
    ProductViewSet,
    ProductAPIView,

)

# API
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    # API
    path('api/v1/', include(router.urls)),
    path('api/v1/generic/products', ProductListGeneric.as_view()), # Recommended
    path('api/v1/generic/products/<int:pk>', ProductDetailGeneric.as_view()), # Recommended

    path('api/v1/mixins/products', ProductListMixins.as_view()),
    path('api/v1/mixins/products/<int:pk>', ProductDetailMixins.as_view()),

    path('api/v1/apiview/products', ProductAPIView.as_view()),
    path('api/v1/apiview/products/<int:pk>', ProductAPIView.as_view()),

    # VIEW
    path ('', base, name='base'),
    path ('clear', clear_cache, name='logout'),
    path ('add', form, name='form'),
    path ('product/<int:product_id>', product_get, name='product_id')
]