# products/views.py
from django.shortcuts import render # Keep for other views if any
from django.views.generic import ListView # Import ListView
from .models import Product
from .forms import ProductSearchForm
# from django.db.models import Q # Keep if using complex Q objects in manager
# from django.utils.translation import gettext_lazy as _
# from django.utils.translation import gettext

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        sort_option = self.request.GET.get('sort')
        queryset = Product.objects.search_and_sort(query=query, sort_option=sort_option)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_term = self.request.GET.get('q', '')
        # Instantiate the form with initial data from the request (if any)
        context['search_form'] = ProductSearchForm(initial={'q': search_term})
        context['page_title'] = 'لیست محصولات'
        # context['search_query'] = search_term # No longer strictly needed if form handles display of q

        sort_option = self.request.GET.get('sort')
        valid_sort_options_keys = ['date_asc', 'date_desc', 'name_asc', 'name_desc', 'brand_asc', 'brand_desc']
        context['sort_option'] = sort_option if sort_option in valid_sort_options_keys else 'date_desc'

        return context

