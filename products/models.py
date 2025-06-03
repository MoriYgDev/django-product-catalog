# products/models.py
from django.db import models
from django.urls import NoReverseMatch, reverse 
# from django_jalali.db import models as jmodels # Uncomment if Jalali is working

# Step 1: Define a custom QuerySet
class ProductQuerySet(models.QuerySet):
    def search(self, query=None):
        if query:
            # Example for multi-field search:
            # return self.filter(
            #     models.Q(name__icontains=query) |
            #     models.Q(description__icontains=query) | # If you want to search description
            #     models.Q(brand__icontains=query)
            # )
            return self.filter(name__icontains=query)
        return self

    def sort_by(self, sort_option=None):
        order_by_field = '-created_at' # Default sort
        valid_sort_options = {
            'date_asc': 'created_at',
            'date_desc': '-created_at',
            'name_asc': 'name',
            'name_desc': '-name',
            'brand_asc': 'brand',
            'brand_desc': '-brand',
        }
        if sort_option in valid_sort_options:
            order_by_field = valid_sort_options[sort_option]
        
        return self.order_by(order_by_field)

# Step 2: Define a custom Manager
class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all_active(self): # Example of another manager method
        return self.get_queryset() # Add any "active" filters if needed, e.g. .filter(is_active=True)

    def search_and_sort(self, query=None, sort_option=None):
        return self.get_queryset().search(query).sort_by(sort_option)


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

    # Step 3: Assign the custom manager
    objects = ProductManager() # Replace default manager

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Returns the URL to access a particular product instance."""
        # Assuming you will create a URL pattern named 'product_detail'
        # in your 'products' app namespace that takes a 'pk' (primary key).
        # If you don't have a detail view yet, this will cause an error
        # if called. You can create the URL and view later.
        # For now, this prepares your model.
        # If you decide not to have a detail page, you can remove this method
        # or have it return None or '#'.
        try:
            return reverse('products:product_detail', kwargs={'pk': self.pk})
        except NoReverseMatch: # Catch error if URL isn't defined yet
            return "#" # Return a placeholder or handle appropriately


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        # Optional: Add default ordering if you like
        # ordering = ['-created_at']