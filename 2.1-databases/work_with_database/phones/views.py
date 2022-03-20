from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sorted_by = request.GET.get('sort', 'name')
    template = 'catalog.html'
    if sorted_by == 'name':
        phones = Phone.objects.order_by('name')
    elif sorted_by == 'min_price':
        phones = Phone.objects.order_by('price')
    elif sorted_by == 'max_price':
        phones = Phone.objects.order_by('-price')
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
