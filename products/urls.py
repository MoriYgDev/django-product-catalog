from django.urls import path
from . import views # Import views from the current app

app_name = 'products' # This is good practice for namespacing URLs

urlpatterns = [
    path('', views.product_list_view, name='list'),
    # Example: path('another-page/', views.another_view, name='another'),
]