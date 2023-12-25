from django.contrib import admin
from .models import Post, Contact, UserProfile
# Register your models here.
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    # list_display = ['id','title','desc','__str__']
    list_display = ['id','title','desc','post_by']

@admin.register(Contact)
class ContaceAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','mob','address']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user','image']