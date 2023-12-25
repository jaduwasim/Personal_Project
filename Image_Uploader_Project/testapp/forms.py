from django import forms
from .models import ImageModelClass

class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageModelClass
        fields = '__all__'
        labels = {'pic':''}