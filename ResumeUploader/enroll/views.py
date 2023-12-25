from django.shortcuts import render
from .models import Profile
from .forms import ProfileForm
from django.contrib import messages
# Create your views here.

def home_view(request):
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Inserted Success')
            all_data = Profile.objects.all()
            return render(request, 'enroll/data.html',{'data':all_data})
    return render(request, 'enroll/home.html',{'form':form})

def data_view(request):
    all_data = Profile.objects.all()
    return render(request, 'enroll/data.html',{'data':all_data})