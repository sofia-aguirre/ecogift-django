from django.shortcuts import render, redirect
from django.conf import settings
from .models import Category, Product

# Create your views here.

def landing(request):
    return render(request, 'eco_app/landing.html')

# CATEGORY READ FUNCTIONS
def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'eco_app/categories_list.html', {'categories': categories})

def category_detail(request, pk):
    category = Category.objects.get(id=pk)
    products = Product.objects.filter(category__exact=category).order_by('model')
    # get(name=category.name)
    return render(request, 'eco_app/categories_detail.html', {'category': category,
    'products':products
    })

# def category_logistics(request, pk):
#     category = Category.objects.get(id=pk)
#     return render(request, 'eco_app/category_logistics.html', {'category': category})

# PRODUCT READ FUNCTIONS
# def product_list(request):
#     products = Product.objects.all()
#     categories = Category.objects.all()
#     return render(request, 'eco_app/product_list.html', {'products': products, 'categories': categories})

def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'eco_app/product_detail.html', {'product': product})
