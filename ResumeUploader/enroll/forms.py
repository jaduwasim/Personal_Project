from django import forms
from .models import Profile
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['id','name','email','dob','state','gender','location','pimage','rdoc']