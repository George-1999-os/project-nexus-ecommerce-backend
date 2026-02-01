from django.contrib import admin
from django.urls import path, include
from products.views import home
from rest_framework import routers, permissions
from products.views import ProductViewSet
from categories.views import CategoryViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# DRF router for Products and Categories
router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'categories', CategoryViewSet, basename='category')

# Swagger / OpenAPI schema
schema_view = get_schema_view(
    openapi.Info(
        title="E-Commerce Backend API",
        default_version='v1',
        description="Backend API for Product Catalog and Authentication",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', home),  # 👈 ROOT URL FIX
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    # Swagger / Redoc
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
