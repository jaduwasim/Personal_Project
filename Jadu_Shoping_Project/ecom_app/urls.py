from django.urls import path
from ecom_app.views import (
    home, product_detail, add_to_cart, buy_now, profile, address,
    orders, change_password, mobile, login, customer_registration, checkout,
    laptop, forget_password,
)

urlpatterns = [
    path('', home),
    path('product-detail/', product_detail, name='product-detail'),
    path('cart/', add_to_cart, name='add-to-cart'),
    path('buy/', buy_now, name='buy-now'),
    path('profile/', profile, name='profile'),
    path('address/', address, name='address'),
    path('orders/', orders, name='orders'),
    path('changepassword/',change_password, name='changepassword'),
    path('mobile/', mobile, name='mobile'),
    path('login/', login, name='login'),
    path('registration/', customer_registration, name='customerregistration'),
    path('checkout/', checkout, name='checkout'),
    path('laptop/', laptop , name='laptop'),
    path('forget-password/', forget_password, name='forgetpassword')
]