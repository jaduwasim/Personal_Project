from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.views import View
from .models import Product, Customer, Cart, OrderPlaced
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.utils.decorators import method_decorator

class ProductView(View):
 def get(self, request):
  top_wear = Product.objects.filter(category='TW')
  bottom_wear = Product.objects.filter(category='BW')
  mobile = Product.objects.filter(category='M')
  laptop = Product.objects.filter(category='L')
  return render(request, 'app/home.html', {'top_wear':top_wear, 'bottom_wear':bottom_wear, 'mobile':mobile, 'laptop':laptop})

class product_detail(View):
    def get(self, request, pk):
        totalitem = 0
        product = Product.objects.get(pk=pk)
        print('product:',product)
        item_already_in_cart =False
        if request.user.is_authenticated:
          totalitem = len(Cart.objects.filter(user=request.user))
          item_already_in_cart = Cart.objects.filter(Q(product=product.id)&Q(user = request.user)).exists()
        return render(request, 'app/productdetail.html', {'product':product, 'item_already_in_cart':item_already_in_cart })

@login_required
def add_to_cart(request):
 user = request.user
 item_alredy_in_cart = False
 product = request.GET.get('prod_id')
 item_alredy_in_cart = Cart.objects.filter(Q(product=product) & Q(user=user)).exists()
 if item_alredy_in_cart == False:
  product_title = Product.objects.get(id=product)
  Cart(user=user, product=product_title).save()
  messages.success(request, 'Product Added to Cart Succesfully!!')
  return redirect('/cart')
 else:
   return redirect('/cart')

@login_required
def show_cart(request):
	totalitem = 0
	if request.user.is_authenticated:
		totalitem = len(Cart.objects.filter(user=request.user))
		user = request.user
		cart = Cart.objects.filter(user=user)
		amount = 0.0
		shipping_amount = 70.0
		totalamount=0.0
		cart_product = [p for p in Cart.objects.all() if p.user == request.user]
		print(cart_product)
		if cart_product:
			for p in cart_product:
				tempamount = (p.quantity * p.product.discounted_price)
				amount += tempamount
				totalamount = amount+shipping_amount
			return render(request, 'app/addtocart.html', {'carts':cart, 'amount':amount, 'totalamount':totalamount, 'totalitem':totalitem})
		else:
			return render(request, 'app/emptycart.html', {'totalitem':totalitem})
	else:
		return render(request, 'app/emptycart.html', {'totalitem':totalitem})

def plus_cart(request):
  if request.method == 'GET':
    prod_id = request.GET['prod_id']
    c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
    c.quantity += 1
    c.save()
    amount = 0.0
    shipping_amount = 70.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    for p in cart_product:
      tempampount = (p.quantity * p.product.discounted_price)
      amount += tempampount
    data = {
      'quantity':c.quantity,
      'amount':amount,
      'totalamount':amount+shipping_amount
    }
    return JsonResponse(data)
  else:
    return HttpResponse("")

def minus_cart(request):
  print('minus cart')
  if request.method == 'GET':
    prod_id = request.GET['prod_id']
    c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
    c.quantity -= 1
    c.save()
    amount = 0.0
    shipping_amount = 70.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    for p in cart_product:
      tempamount = (p.quantity * p.product.discounted_price)
      amount += tempamount
      data = {
        'quantity':c.quantity,
        'amount':amount,
        'totalamount':amount+shipping_amount
      }
    return JsonResponse(data)
  else:
    return HttpResponse("")
  
def remove_cart(request):
  if request.method == 'GET':
    prod_id = request.GET['prod_id']
    c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
    c.delete()
    amount = 0.0
    shipping_amount = 70.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    for p in cart_product:
      tempamount = (p.quantity * p.product.discounted_price)
      amount += tempamount
    data ={
      'amount':amount,
      'totalamount':amount+shipping_amount
    }
    # messages.success(request, 'Item Remove From Cart Successfully!!')
    return JsonResponse(data)
  else:
    return HttpResponse("")
  

@login_required
def buy_now(request):
 return render(request, 'app/buynow.html')


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
 def get(self, request):
  form = CustomerProfileForm()
  return render(request, 'app/profile.html', {'form':form})
 
 def post(self, request):
  form = CustomerProfileForm(request.POST)
  if form.is_valid():
    usr = request.user
    name = form.cleaned_data['name']
    locality = form.cleaned_data['locality']
    city = form.cleaned_data['city']
    state = form.cleaned_data['state']
    zipcode = form.cleaned_data['zipcode']
    reg = Customer(user=usr, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
    reg.save()
    messages.success(request, 'Profile Updated Successfully!!')
  return render(request, 'app/profile.html', {'form':form, 'active':'btn-primary'})
 
@login_required
def address(request):
 add = Customer.objects.filter(user=request.user)
 return render(request, 'app/address.html', {'address':add, 'active':'btn-primary'})

def orders(request):
 op = OrderPlaced.objects.filter(user=request.user)
 
 return render(request, 'app/orders.html', {'order_placed':op})

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request,data=None):
  if data==None:
   mobile = Product.objects.filter(category='M')
  elif data == 'Redmi' or data == 'Samsung':
   mobile = Product.objects.filter(category='M').filter(brand=data)
  elif data == 'below':
   mobile = Product.objects.filter(category='M').filter(discounted_price__lt = 10000)
  elif data == 'above':
   mobile = Product.objects.filter(category='M').filter(discounted_price__gt=10000)

  return render(request, 'app/mobile.html', {'mobile':mobile})

def login(request):
 return render(request, 'app/login.html')

class customerregistration(View):
 def get(self, request):
   form = CustomerRegistrationForm()
   return render(request, 'app/customerregistration.html', {'form':form})
 
 def post(self, request):
  form = CustomerRegistrationForm(request.POST)
  if form.is_valid():
   messages.success(request, 'Congratulation!! Registrations Successfully.')
   form.save()
  return render(request, 'app/customerregistration.html', {'form':form})

@login_required
def checkout(request):
 user = request.user
 address = Customer.objects.filter(user=user)
 cart_item = Cart.objects.filter(user=request.user)
 amount =0.0
 shipping_amount = 70.0
 total_amount = 0.0
 cart_product = [p for p in Cart.objects.all() if p.user==request.user]
#  print('Cart Product:',cart_product)
 if cart_product:
  for p in cart_product:
    # print(f'p: {p}')
    tempamount = (p.quantity * p.product.discounted_price)
    # print('tempamount:',tempamount)
    amount += tempamount
    # print('amount:', amount)
  total_amount = amount + shipping_amount
 return render(request, 'app/checkout.html',{'address':address, 'cartitem':cart_item, 'total_amount':total_amount})

@login_required
def Payment_DoneView(request):
  cust_id = request.GET.get('custid')
  print('custmer id',cust_id)
  user = request.user
  print(f'User : {user}')
  cart_id = Cart.objects.filter(user=user)
  print(f'cart id: {cart_id}')
  customer = Customer.objects.get(id=cust_id)
  print(f'Customer:{customer}')
  for cid in cart_id:
    OrderPlaced(user=user, customer=customer, product=cid.product, quantity=cid.quantity).save()
    cid.delete()
  return redirect('orders')

def laptop(request, data=None):
 if data==None:
  laptop = Product.objects.filter(category='L')
 elif data == 'Apple' or data == 'Accer':
  laptop = Product.objects.filter(category='L').filter(brand=data)
 elif data == 'below':
  laptop = Product.objects.filter(category='L').filter(discounted_price__lt = 15000)
 elif data == 'above':
  laptop = Product.objects.filter(category='L').filter(discounted_price__gt=15000)
 return render(request, 'app/laptop.html', {'laptop':laptop})

def top_wear(request, data=None):
 if data ==None:
  top_wear = Product.objects.filter(category='TW')
 elif data == 'T-shirt' or data == 'Shirt':
  top_wear = Product.objects.filter(category='TW').filter(brand=data)
 elif data == 'below':
  top_wear = Product.objects.filter(category='TW').filter(discounted_price__lt = 10000)
 elif data == 'above':
  top_wear = Product.objects.filter(category='TW').filter(discounted_price__gt = 10000)
 return render(request, 'app/topwear.html', {'top_wear':top_wear})

def bottom_wear(request, data=None):
 if data == None:
  bottom = Product.objects.filter(category='BW')
 elif data == 'Jeans' or data == 'Paint':
  bottom = Product.objects.filter(category='BW').filter(brand=data)
 elif data == 'below':
  bottom = Product.objects.filter(category='BW').filter(discounted_price__lt = 10000)
 elif data == 'above':
  bottom = Product.objects.filter(category='BW').filter(discounted_price__gt = 10000)
 return render(request, 'app/bottomwear.html', {'bottomwear':bottom})

def forget_password(request):
 return render(request, 'app/forgetpassword.html')