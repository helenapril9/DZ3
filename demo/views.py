from django.shortcuts import render, redirect
from .models import Phone

# Create your views here.
def show_catalog(request):
    phones = Phone.objects.all()
    for phone in phones:
        return render(request, 'catalog.html',{'phones': phones})

def show_catalog_sort(request):
    sort = request.GET['sort']
    if sort == 'max_price':
        phones = Phone.objects.order_by('-price')
    if sort == 'min_price':
        phones = Phone.objects.order_by('price')
    if sort == 'name':
        phones = Phone.objects.order_by('name')
    return render(request, 'catalog.html',{'phones': phones})

def show_product(request, model):
    phones = Phone.objects.filter(slug=model)
    return render(request, 'product.html',{'phones': phones})


