from django.urls import path
from enroll.views import HomeView, CandidteDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView.as_view()),
    path('<int:pk>/', CandidteDetailView.as_view(), name='candidate'),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)