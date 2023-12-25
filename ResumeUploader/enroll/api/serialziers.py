from rest_framework import serializers
from enroll.models import Profile

class ProfileSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id','name','email','dob','state','gender','location','pimage','rdoc']