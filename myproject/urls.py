from django.contrib import admin # Keep this import for admin.autodiscover if needed or for other uses
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Import your custom admin site instance
from .admin import admin_site # Assuming myproject/admin.py

# Your existing admin site customizations for titles can be applied to your custom instance
admin_site.site_header = "Project Admin Panel"  # English header
admin_site.site_title = "Project Admin"       # English browser tab title
admin_site.index_title = "Welcome to the Admin Panel" # English index title

urlpatterns = [
    # path('admin/', admin.site.urls), # Comment out or remove the old line
    path('admin/', admin_site.urls),   # Use your custom admin_site's URLs
    path('', include('products.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)