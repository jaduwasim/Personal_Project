from django.urls import path
from static_app import views
urlpatterns = [
    path('', views.home),
    path('product-detail/', views.product_detail, name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('login/', views.login, name='login'),
    path('registration/', views.customerregistration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('laptop/', views.laptop, name='laptop'),
    path('top-wear/', views.top_wear, name='topwear'),
    path('bottom-wear/', views.bottom_wear, name='bottomwear'),
    path('forget-password/', views.forget_password, name='forgetpassword'),
]
