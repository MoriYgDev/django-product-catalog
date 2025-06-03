from django import template
import math # Not strictly needed for this version, but good to have for number ops

register = template.Library()

@register.filter(name='rial_format') # We're naming our filter 'rial_format'
def rial_format(value):
    """
    Formats a number with periods as thousands separators.
    e.g., 10000000 -> "10.000.000"
    Assumes price is a whole number as decimal_places=0.
    """
    if value is None: # Handle None if it can occur
        return "" 
    
    try:
        # Ensure value is treated as an integer (since your price has decimal_places=0)
        num_int = int(value)
        
        # Use f-string formatting to get comma separators first
        formatted_with_commas = f"{num_int:,}"
        
        # Replace commas with periods
        formatted_with_periods = formatted_with_commas.replace(',', '.')
        
        return formatted_with_periods
    except (ValueError, TypeError):
        # If conversion fails, return the original value or an error indicator
        return str(value)