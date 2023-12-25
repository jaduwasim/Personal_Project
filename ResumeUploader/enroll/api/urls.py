from django.urls import path, include
from enroll.api.views import ProfileAPI
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('api', ProfileAPI, basename='api')


urlpatterns = [
    path('', include(router.urls)),
]