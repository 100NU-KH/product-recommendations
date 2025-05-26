from rest_framework import serializers
from products.models import Product
from recommend_engine import Recommender

class ProductListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ('id', 'name', 'product_image',
                  'description', 'category', 'price')


class ProductDetailSerializer(serializers.ModelSerializer):
    
    recommendations = serializers.SerializerMethodField()
    
    def get_recommendations(self, obj):
        return ProductListSerializer(
            Recommender().get_similar_products(obj.id, 10),
            many=True
        ).data

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'product_image',
            'description', 'category', 'price',
            'recommendations'
        )
        depth = 1
        