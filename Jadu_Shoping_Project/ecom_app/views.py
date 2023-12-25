from django.shortcuts import render

def home(request):
    return render(request, 'ecom_app/home.html')

def product_detail(request):
    return render(request, 'ecom_app/productdetail.html')

def add_to_cart(request):
    return render(request, 'ecom_app/addtocart.html')

def buy_now(request):
    return render(request, 'ecom_app/buynow.html')

def profile(request):
    return render(request, 'ecom_app/profile.html')

def address(request):
    return render(request, 'ecom_app/address.html')

def orders(request):
    return render(request, 'ecom_app/orders.html')

def change_password(request):
    return render(request, 'ecom_app/changepassword.html')

def mobile(request):
    return render(request, 'ecom_app/mobile.html')

def login(request):
    return render(request, 'ecom_app/login.html')

def customer_registration(request):
    return render(request, 'ecom_app/customerregistration.html')

def checkout(request):
    return render(request, 'ecom_app/checkout.html')

def laptop(request):
    return render(request, 'ecom_app/laptop.html')

def forget_password(request):
    return render(request, 'ecom_app/forgetpassword.html')