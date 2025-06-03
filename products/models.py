# products/models.py
from django.db import models
# from django_jalali.db import models as jmodels # Uncomment if Jalali is working

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Product Name")
    price = models.DecimalField(max_digits=15, decimal_places=0, verbose_name="Price")
    entry_date = models.DateField(verbose_name="Entry Date") # Or jmodels.jDateField
    brand = models.CharField(max_length=100, null=True, blank=True, verbose_name="Brand")
    description = models.TextField(null=True, blank=True, verbose_name="Description")
    image = models.ImageField(upload_to='product_images/', null=True, blank=True, verbose_name="Image")
    vendor = models.CharField(max_length=200, null=True, blank=True, verbose_name="Vendor") # New field

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At") # Or jmodels.jDateTimeField
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At") # Or jmodels.jDateTimeField

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"