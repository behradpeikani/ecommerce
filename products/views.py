from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
from carts.forms import AddCartForm
from django.core.paginator import Paginator

# Create your views here.

def products_list(request):
	products = Product.objects.filter(is_active=True)

	paginator = Paginator(products, 9)
	page_number = request.GET.get('page')
	products = paginator.get_page(page_number)
	return render(request, 'products/products_list.html', {"products": products})

def single_product(request, slug):
	product = get_object_or_404(Product, slug=slug, is_active=True)
	form = AddCartForm()
	return render(request, 'products/single_product.html', {"product": product, "form": form})

def category_view(request, slug):
	category = get_object_or_404(Category, slug=slug)
	products = Product.objects.filter(category=category, is_active=True)

	paginator = Paginator(products, 2)
	page_number = request.GET.get('page')
	products = paginator.get_page(page_number)
	return render(request, 'products/category.html', {'category': category, 'products': products})
