from django.shortcuts import render, get_object_or_404, redirect
from .utils import Cart
from products.models import Product
from .forms import AddCartForm

# Create your views here.

def cart_detail(request):
	cart = Cart(request)
	return render(request, 'carts/cart_detail.html', {"cart": cart})

def cart_add(request, product_id):
	cart = Cart(request)
	product = get_object_or_404(Product, id=product_id)

	if request.method == 'POST':
		form = AddCartForm(request.POST or None)
		if form.is_valid():
			cart.add(product=product, quantity=form.cleaned_data['quantity'])
		return redirect('carts:cart_detail')

def cart_remove(request, product_id):
	cart = Cart(request)
	product = get_object_or_404(Product, id=product_id)
	cart.remove(product)
	return redirect('carts:cart_detail')
