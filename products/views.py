from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    CRUD API for Products
    - Filtering by category and active status
    - Ordering by price, name, or creation date
    - Search by name or description
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering, ordering, and search
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['category', 'is_active']
    ordering_fields = ['price', 'name', 'created_at']
    search_fields = ['name', 'description']
