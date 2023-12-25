from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SignupForm, LoginForm, MyPostForm, ContactForm, UserProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Post, UserProfile
from django.contrib.auth.models import User, Group



def Home_View(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts':posts})

def About_View(request):
    return render(request, 'blog/about.html')

def Contact_View(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'thanks for Contact Us, We will get back to you...')
            return render(request,'blog/home.html')
    return render(request, 'blog/contact.html',{'forms':form})

def Dashboard_View(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        print('user:',user)
        user_profile = User.objects.filter(username=user)
        # print(f'User Profile: {user_profile}')
        # for user in user_profile:
        #     print('id:',user.id)
        #     print('profile pic:', user.userprofile.image.url)
        full_name = user.get_full_name()
        gps = user.groups.all()
        return render(request, 'blog/dashboard.html', {'posts':posts, 'full_name':full_name,'groups':gps, 'user_profile':user_profile})
    else:
        return HttpResponseRedirect('/login/')

def Login_View(request):
    if not request.user.is_authenticated:
        form = LoginForm()
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'You Are Login Now!!')
                    return HttpResponseRedirect('/userprofile/')
        return render(request, 'blog/login.html', {'forms':form})
    else:
        messages.info(request, 'Yor are already Login')
        return render(request, 'blog/dashboard.html')

def Logout_View(request):
    if request.user.is_authenticated:
        logout(request,)
        messages.info(request,'Thanks for Using Our Application')
        return render(request, 'blog/logout.html')
    else:
        return render(request, 'blog/logout.html')

def Signup_View(request):
    if not request.user.is_authenticated:
        form = SignupForm()
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                user = form.save()
                group = Group.objects.get(name='Author')
                user.groups.add(group)
                messages.success(request,'Congratulation!! Now You are an Author,')
                return render(request, 'blog/signupdone.html')
        return render(request, 'blog/singup.html',{'forms':form})
    else:
        messages.info(request, 'You are login Right Now, For creating another Account Please Logout First')
        return render(request, 'blog/dashboard.html')
    
# Add Post
def Add_Post(request):
    if request.user.is_authenticated:
        form = MyPostForm()
        if request.method == 'POST':
            form =MyPostForm(request.POST)        
            if form.is_valid():
                user = request.user
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                data = Post(user=user, title=title, desc=desc)
                data.save()
                messages.success(request,'Your New Post Created Successfully!!')
                return render(request, 'blog/addpost.html')
        return render(request, 'blog/addpost.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')
    
# Update Post
def Update_Post(request, id):
    if request.user.is_authenticated:
        post_data = Post.objects.get(pk=id)
        form = MyPostForm(instance=post_data)
        if request.method == 'POST':
            form = MyPostForm(request.POST, instance=post_data)
            if form.is_valid():
                form.save()
                messages.success(request, 'Post Has Update!!')
                return render(request, 'blog/updatepost.html')
        return render(request, 'blog/updatepost.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')

# Delete Post
def Delete_Post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            post_data = Post.objects.get(pk=id)
            post_data.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')

# User Profile
def User_Profile_View(request):
    if request.user.is_authenticated:
        print('user:',request.user)
        form = UserProfileForm()
        if request.method == 'POST':
            form = UserProfileForm(request.POST, request.FILES)
            if form.is_valid():
                user = request.user
                image = form.cleaned_data['image']
                data = UserProfile(user=user, image=image)
                data.save()
                return HttpResponseRedirect('/dashboard/')
        return render(request,'blog/userprofile.html',{'forms':form})
    else:
        messages.info(request, 'You Please Login First')
        return render(request, 'blog/login.html')
    
def Profile_Views(request):
    if request.user.is_authenticated:
        user = request.user
        user_profile = User.objects.filter(username=request.user)
        full_name = user.get_full_name()
        gps = user.groups.all()
    return render(request,'blog/profile.html', {'user_profile':user_profile, 'full_name':full_name,'groups':gps})

def Profile_Deatil_View(request, id):
    user = Post.objects.get(pk=id)
    return  render(request,'blog/profiledetail.html',{'user':user})