# products/templatetags/product_extras.py
from django import template
from django.urls import reverse
from django.http import QueryDict # Needed to easily build query strings

register = template.Library()

@register.filter(name='rial_format')
def rial_format(value):
    # ... your existing rial_format filter code ...
    if value is None:
        return ""
    try:
        num_int = int(value)
        formatted_with_commas = f"{num_int:,}"
        formatted_with_periods = formatted_with_commas.replace(',', '.')
        return formatted_with_periods
    except (ValueError, TypeError):
        return str(value)

@register.simple_tag(takes_context=True)
def sort_button_context(context, sort_field_name, display_text):
    """
    Generates context for a sort button.
    'sort_field_name' should be the base field, e.g., 'date', 'name', 'brand'.
    """
    request = context['request']
    current_sort_param = request.GET.get('sort')
    current_search_query = request.GET.get('q')

    is_active = False
    icon_html = "" # Will hold the i tag HTML
    # Determine the 'next' sort value for this button
    # Default to ascending if not currently sorted by this field or if sorted descending
    next_sort_value = f"{sort_field_name}_asc"

    if current_sort_param == f"{sort_field_name}_asc":
        is_active = True
        icon_html = '<i class="bi bi-arrow-up"></i>'
        next_sort_value = f"{sort_field_name}_desc" # Toggle to descending
    elif current_sort_param == f"{sort_field_name}_desc":
        is_active = True
        icon_html = '<i class="bi bi-arrow-down"></i>'
        next_sort_value = f"{sort_field_name}_asc" # Toggle back to ascending

    # Build the URL with query parameters
    query_params = QueryDict(mutable=True)
    query_params['sort'] = next_sort_value
    if current_search_query:
        query_params['q'] = current_search_query

    url = f"{reverse('products:list')}?{query_params.urlencode()}"

    button_class = "btn btn-primary" if is_active else "btn btn-outline-secondary"

    return {
        'url': url,
        'button_class': button_class,
        'display_text': display_text,
        'icon_html': icon_html, # Pass the generated icon HTML
    }