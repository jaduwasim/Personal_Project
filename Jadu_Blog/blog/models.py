from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    desc = models.TextField()

    def post_by(self):
        return self.user.first_name + ' ' + self.user.last_name
    
    def __str__(self):
        return self.user.username
    class Meta:
        db_table = 'Post'

class Contact(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    mob = models.IntegerField()
    address = models.CharField(max_length=80)
    
    class Meta:
        db_table = 'contact'
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
    image = models.ImageField(upload_to='porductimage')
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        db_table = 'userprofile'