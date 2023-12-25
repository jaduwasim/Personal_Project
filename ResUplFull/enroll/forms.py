from django import forms
from enroll.models import Resume

GENDER_CHICES = [
    ('Male','Male'),
    ('Femail','Female')
]

JOB_CITY_CHOICE = [
    ('Delhi','Delhi'),
    ('Pune','Pune'),
    ('Noida','Noida'),
    ('Bihar','Bihar'),
    ('Mumbai','Mumbai'),
    ('Dhanbad','Dhanbad')
]

class ResumeForms(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHICES, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(label='Prefered Job Location', choices=JOB_CITY_CHOICE, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Resume
        fields = ['name','dob','gender','locality','city','pin','state','mobile','job_city','profile_image','my_file']
        labels = {
            'name':'Full Name', 
            'dob':'Date of Birth',
            'pin':'Pin Code',
            'mobile':'Mobile',
            'email':'Email Id',
            'profile_image':'Profile Image',
            'my_file':'Documents'
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }