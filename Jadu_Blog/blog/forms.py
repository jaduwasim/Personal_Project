from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordResetForm, SetPasswordForm
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation
from .models import Post, Contact, UserProfile

def validate_email(value):
    if User.objects.filter(email = value).exists():
        raise ValidationError((f'{value} alredy taken'), params ={'value':value})

class SignupForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password(Again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(required= True, label='Email Id', validators=[validate_email],widget=forms.EmailInput(attrs={'class':'form-control'}))

    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {
            'first_name':'First Name',
            'last_name':'Last Name',
        }
        widgets= {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
        }

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

    # password forget
class MyPasswordResetForm(PasswordResetForm):
    email = forms.CharField(required= True, label='Email Id', widget=forms.EmailInput(attrs={'class':'form-control'}))

    def clean_email(self):
        email_id = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email_id).exists():
            raise ValidationError('This is not Existing user, please Enter Existing Email')
        return email_id

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password', strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label='Confirm New Password', strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control'}))

class MyPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user',)
        labels = {
            'title':'Title',
            'desc':'Description'
        }
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'desc':forms.Textarea(attrs={'class':'form-control'}),
        }
    
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        labels ={
            'name':'Name',
            'email':'Email Address',
            'mob':'Mobile Number',
            'address':'Address'
        }
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'mob':forms.NumberInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'})
        }
    
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('image',)
        labels = {'image':'Upload Image:'}
  