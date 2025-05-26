from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from products.models import Product
from apis.product.serializers import ProductListSerializer


class ProductListApiView(ListAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filterset_fields = ['name']