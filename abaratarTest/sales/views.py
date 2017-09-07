from django.shortcuts import render
from .models import Product

# Create your views here.

def index_view(request):
    '''
    Render initial view: App init
    '''
    context = { 'products': Product.objects.all() }

    return render(request, 'pages/index.html', context)

def prepare_view(request, id):
    '''
    Render initial view: App init
    '''
    product =  Product.objects.filter(id=id)[:1].get()
    return render(request, 'pages/prepareBuy.html', {'product': product})
