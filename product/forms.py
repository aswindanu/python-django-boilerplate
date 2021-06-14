from django import forms
from product.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ["name", "description", "images", "price", "quantity"]
