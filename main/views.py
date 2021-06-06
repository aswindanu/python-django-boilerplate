from django.shortcuts import render, redirect
from .models import Main 
from .forms import MainForm


def base(request):
    return render(request, 'stuff.html', { 'Main': Main.objects.all() })

def form(request):
    if request.method == "POST":
        form = MainForm(request.POST, request.FILES)
        print("REQUEST", request, "form", form, "POST", request.POST, "FILES",request.FILES)
        if form.is_valid():
            form.save()
            return redirect('base')  # call with name from url 'base'
    else:
        form = MainForm()
    return render(request, 'form.html',{'form': form })

def main_get(request, main_id):
    return render(request, 'stuff.html',{'Main': Main.objects.get(pk=main_id) })
