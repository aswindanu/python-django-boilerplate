from django.conf import settings
from django.core.cache import cache
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from .models import Product 
from .forms import ProductForm

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

def base(request):
    return render(request, 'product_list.html', { 'Product': Product.objects.all() })

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

def clear_cache(request):
    # Clear cache
    cache.clear()
    return HttpResponseRedirect('/')

@cache_page(CACHE_TTL)
def product_get(request, product_id):
    return render(request, 'product.html',{'Product': Product.objects.get(pk=product_id) })
