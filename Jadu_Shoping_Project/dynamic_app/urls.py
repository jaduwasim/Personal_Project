from django.urls import path
from dynamic_app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm

urlpatterns = [
    # Home Page
    path('', views.ProductView.as_view()),
    # Cart
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),
    path('buy/', views.buy_now, name='buy-now'),
    # payment 
    path('paymentdone/', views.Payment_DoneView, name = 'paymentdone'),

    # Profile
    path('profile/', views.ProfileView.as_view(), name='profile'),
    


    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    # Change Passwrod
    path('changepassword/', auth_views.PasswordChangeView.as_view(template_name='app/changepassword.html', form_class=MyPasswordChangeForm, success_url='/changepassworddone/'), name='changepassword'),
    path('changepassworddone/',auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),

    # Login
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),

    # Logout
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Registration
    path('registration/', views.customerregistration.as_view(), name='customerregistration'),

    path('checkout/', views.checkout, name='checkout'),

    # Product 
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>/', views.mobile, name='mobiledata'),
    path('laptop/', views.laptop, name='laptop'),
    path('laptop/<slug:data>/', views.laptop, name='laptopdata'),
    path('top-wear/', views.top_wear, name='topwear'),
    path('top-wear/<slug:data>/', views.top_wear, name='topweardata'),
    path('bottom-wear/', views.bottom_wear, name='bottomwear'),
    path('bottom-wear/<slug:data>/', views.bottom_wear, name='bottomweardata'),

    # Product Details
    path('product-detail/<int:pk>/', views.product_detail.as_view(), name='product-detail'),

    # Reset Password
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='app/forgetpassword.html', form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class=MySetPasswordForm),name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),

    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
