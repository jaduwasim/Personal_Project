from django.urls import path
from blog import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .forms import MyPasswordResetForm,MySetPasswordForm
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.Home_View, name='home'),
    path('about/',views.About_View, name='about'),
    path('contact/',views.Contact_View, name='contact'),
    path('dashboard/',views.Dashboard_View, name='dashboard'),
    path('login/',views.Login_View, name='login'),
    path('signup/',views.Signup_View, name='singup'),
    path('logout/',views.Logout_View, name='logout'),

    # password forget
    path('password-reset/', PasswordResetView.as_view(template_name='blog/forgetpassword.html', form_class=MyPasswordResetForm), name='password_reset'),
    path('password_reset_done/', PasswordResetDoneView.as_view(template_name='blog/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='blog/password_reset_confirm.html',form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(template_name='blog/password_reset_complete.html'), name='password_reset_complete'),

    # Add Post
    path('addpost/', views.Add_Post, name='addpost'),
    # update post
    path('updatepost/<int:id>/', views.Update_Post, name='updatepost'),
    # Delete Post
    path('delete/<int:id>/', views.Delete_Post, name='deletepost'),
    # User Profile
    path('userprofile/',views.User_Profile_View, name='userprofile'),
    # Profile
    path('profile/', views.Profile_Views, name='profile'),
    # profile Details
    path('profiledetails/<int:id>/', views.Profile_Deatil_View, name='profiledetails')
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)