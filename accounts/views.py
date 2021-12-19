from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .forms import SignInForm, SignUpForm, AddressForm
from .models import User
from .decorators import login_excluded
from orders.models import Order


# Create your views here.

@login_excluded('products:products_list')
def sign_in_view(request):
    if request.method == 'POST':
        form = SignInForm(request.POST or None)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You logged in', 'success')
                return redirect('products:products_list')
            else:
                return messages.error(request, 'Invalid username or password! try again.', 'warning')
    else:
        form = SignInForm()

    return render(request, 'accounts/sign_in.html', {"form": form})

@login_excluded('products:products_list')
def sign_up_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')

            try:
                user = User.objects.create_user(first_name=first_name, last_name=last_name,
                 email=email, password=password)
                user.save()
            except:
                user = None

            if user != None:
                login(request, user)
                messages.success(request, 'Your account has been successfully created', 'success')
                return redirect('accounts:sign_in')
            else:
                messages.info(request, 'Registration unseccessful! try again.')
    else:
        form = SignUpForm()

    return render(request, 'accounts/sign_up.html', {"form": form})


@login_required
def sign_out_view(request):
    logout(request)
    messages.success(request, 'You have been logged out', 'success')
    return redirect('products:products_list')

@login_required
def add_address(request):
    if request.method == "POST":
        form = AddressForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.customer = request.user
            form.save()
            return HttpResponse('Your orders have been submitted.')
    else:
        form = AddressForm()
    return render(request, "accounts/address.html", {"form": form})
