from django.contrib import admin
from .models import Product # Make sure Product model is correctly imported

# Import your custom admin_site from the project level
from myproject.admin import admin_site 

# Import the CORRECT Jalali widgets and the model field types for checking
from django_jalali.admin.widgets import AdminjDateWidget, AdminSplitjDateTime # CORRECTED WIDGET NAMES
from django_jalali.db.models import jDateField, jDateTimeField # These are MODEL fields

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'vendor', 'price', 'entry_date', 'created_at', 'updated_at')
    search_fields = ('name', 'brand', 'vendor', 'description')
    list_filter = ('brand', 'vendor', 'entry_date', 'created_at')

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if isinstance(db_field, jDateTimeField):
            # Override the widget for jDateTimeField with the correct one
            kwargs['widget'] = AdminSplitjDateTime # USE THIS FOR DATETIME
        elif isinstance(db_field, jDateField):
            # Override the widget for jDateField with the correct one
            kwargs['widget'] = AdminjDateWidget # USE THIS FOR DATE

        # Let the parent class create the formfield with our potentially modified kwargs
        return super().formfield_for_dbfield(db_field, request, **kwargs)

# Register with your custom admin_site
admin_site.register(Product, ProductAdmin)