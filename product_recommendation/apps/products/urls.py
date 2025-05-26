from django.urls import path, re_path
from apis.product.views import ProductListApiView, ProductDetailRetrieveAPIView

app_name = 'products'

urlpatterns = [
    path('list', ProductListApiView.as_view()),
    re_path(r'^detail/(?P<pk>\d+)/$', ProductDetailRetrieveAPIView.as_view()),
]