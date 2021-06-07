from django.shortcuts import render, redirect
from .models import Product 
from .forms import ProductForm


def base(request):
    return render(request, 'stuff.html', { 'Product': Product.objects.all() })

def form(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        print("REQUEST", request, "form", form, "POST", request.POST, "FILES",request.FILES)
        if form.is_valid():
            form.save()
            return redirect('base')  # call with name from url 'base'
    else:
        form = ProductForm()
    return render(request, 'form.html',{'form': form })

def main_get(request, product_id):
    return render(request, 'product.html',{'Product': Product.objects.get(pk=product_id) })
