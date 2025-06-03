from django.shortcuts import render
from .models import Product
from django.db.models import Q
from django.utils.translation import gettext_lazy as _ # For models/forms
from django.utils.translation import gettext # For views

# Example in a model:
# class Product(models.Model):
#     name = models.CharField(_("name"), max_length=200)

# Example in a view:
# message = gettext("Operation successful.")

def product_list_view(request):
    products_queryset = Product.objects.all() 
    search_query = request.GET.get('q')
    sort_option = request.GET.get('sort')

    if search_query:
        products_queryset = products_queryset.filter(name__icontains=search_query)
        # Example for multi-field search:
        # products_queryset = products_queryset.filter(
        # Q(name__icontains=search_query) |
        # Q(description__icontains=search_query) |
        # Q(brand__icontains=search_query)
        # )

    # Determine the field and direction for sorting
    order_by_field = '-created_at' # Default
    
    if sort_option:
        if sort_option == 'date_asc':
            order_by_field = 'created_at'
        elif sort_option == 'date_desc':
            order_by_field = '-created_at'
        elif sort_option == 'name_asc':
            order_by_field = 'name'
        elif sort_option == 'name_desc':
            order_by_field = '-name'
        elif sort_option == 'brand_asc':
            # Handle potential None values in brand if you want them last/first
            # For simplicity, this sorts None values first with some databases.
            # from django.db.models.functions import Coalesce
            # products_queryset = products_queryset.annotate(
            # brand_filled=Coalesce('brand', Value('')) # Replace Value('') with a string that sorts last if needed
            # ).order_by('brand_filled')
            order_by_field = 'brand' 
        elif sort_option == 'brand_desc':
            order_by_field = '-brand'
        # else: sort_option is invalid, default_sort_option will be used.
    
    products_queryset = products_queryset.order_by(order_by_field)

    # If no sort_option was provided or it was invalid, set a default for template context
    active_sort_option = sort_option if sort_option in ['date_asc', 'date_desc', 'name_asc', 'name_desc', 'brand_asc', 'brand_desc'] else 'date_desc'

    context = {
        'products': products_queryset,
        'page_title': 'لیست محصولات',
        'search_query': search_query,
        'sort_option': active_sort_option, # Pass the active or default sort option
    }
    return render(request, 'products/product_list.html', context)