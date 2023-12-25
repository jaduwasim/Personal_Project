from django.shortcuts import render, HttpResponseRedirect
from student.forms import SignUpForm, ProfileEditForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from student.forms import LoginForm

# Create your views here.
def home_view(request):
    return render(request, 'student/home.html')

def signup_view(request):
    fm = SignUpForm()
    if request.method=='POST':
        fm = SignUpForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Registered Success, Now You Can Login...')
            return HttpResponseRedirect('/login/')
    return render(request, 'student/signup.html', {'form':fm})

def login_view(request):
    if request.user.is_authenticated:
        messages.success(request, 'You are already Login')
        return render(request, 'student/profile.html')
    else:
        fm = LoginForm()
        if request.method == "POST":
            fm = LoginForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'You are Login Now')
                    return HttpResponseRedirect('/profile/')
            else:
                messages.success(request, 'Invalid Credential...')
                return HttpResponseRedirect('/login/')
        return render(request, 'student/login.html',{'form':fm})

def profile_view(request):
    if request.user.is_authenticated:
        fm = ProfileEditForm(instance=request.user)
        if request.method == "POST":
            fm = ProfileEditForm(request.POST,request.FILES, instance=request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Profile Updated...')
                return HttpResponseRedirect('/profile/')
        return render(request, 'student/profile.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')
    
def logout_view(request):
    logout(request)
    messages.success(request, 'Now You are logout!!!')
    return render(request, 'student/home.html')