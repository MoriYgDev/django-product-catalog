# products/urls.py
from django.urls import path
# from . import views # Old import
from .views import ProductListView # Import the new CBV

app_name = 'products'

urlpatterns = [
    # path('', views.product_list_view, name='list'), # Old path
    path('', ProductListView.as_view(), name='list'), # Use .as_view() for CBVs
]