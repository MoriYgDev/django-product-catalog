# products/forms.py
from django import forms

class ProductSearchForm(forms.Form):
    q = forms.CharField(
        required=False, # Search is optional
        label='',       # We won't show a <label> tag, placeholder is enough
        widget=forms.TextInput(
            attrs={
                'placeholder': 'نام محصول را جستجو کنید...',
                'class': 'form-control', # Bootstrap class
                'id': 'searchInput',     # Keep your existing ID if needed for JS/CSS
                'autocomplete': 'off',
            }
        )
    )
    # You could add more fields here for advanced search later (e.g., brand, price range)