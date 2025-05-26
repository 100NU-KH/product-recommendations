from rest_framework.generics import RetrieveAPIView
from products.models import Product
from apis.product.serializers import ProductDetailSerializer


class ProductDetailRetrieveAPIView(RetrieveAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer