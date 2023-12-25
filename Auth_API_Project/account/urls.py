from django.urls import path
from account.views import (UserRegistrationView, 
                           UserLoginView,
                           UserProfileView,
                           UserChangePasswordView,
                           SendPasswordResetEmailView,
                           UserPasswordResetView)

urlpatterns = [
    path('registration/',UserRegistrationView.as_view(), name='registration'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name='change-password'),
    path('send-reset-password-email/',SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
]


# https://github.com/geekyshow1/djangoauthapi1/tree/master/account
# https://python.plainenglish.io/how-to-send-email-with-verification-link-in-django-efb21eefffe8