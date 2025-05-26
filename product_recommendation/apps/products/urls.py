from django.urls import path, include
from apis.product.views import ProductListApiView

app_name = 'products'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('list', ProductListApiView.as_view())
]