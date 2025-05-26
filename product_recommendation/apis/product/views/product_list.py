from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from products.models import Product
from apis.product.serializers import ProductDetailSerializer


class ProductListApiView(ListAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    filterset_fields = ['name']