from django.contrib import admin
from .models import ImageModelClass

@admin.register(ImageModelClass)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','pic','time']