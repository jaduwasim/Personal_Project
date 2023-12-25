from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from student.models import StudentUser

custom_widget = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'class_name':forms.Select(attrs={'class':'form-control'}),
        }
class SignUpForm(UserCreationForm):
    date_of_birth = forms.DateField(label="Date of Birth",
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date", 'class':'form-control'}),
        input_formats=["%Y-%m-%d"])
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password(Again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = StudentUser
        fields = ['username','first_name','last_name','email','image','date_of_birth','phone','class_name']
        labels = {'first_name':'First Name','last_name':'Last Name','email':'Email Address','phone':'Mobile No.','image':'Profile Picture','class_name':'Class'}
        widgets = custom_widget

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='User Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

class ProfileEditForm(UserChangeForm):
    password =None
    date_of_birth = forms.DateField(label="Date of Birth",
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date", 'class':'form-control'}),
        input_formats=["%Y-%m-%d"])
    class Meta:
        model = StudentUser
        fields = ['first_name','last_name','email','image','date_of_birth','phone','class_name']
        widgets = custom_widget