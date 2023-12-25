from django.urls import path
from enroll.views import home_view, data_view

urlpatterns = [
    path('', home_view),
    path('data/', data_view),
]