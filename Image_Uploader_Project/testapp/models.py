from django.db import models

# Create your models here.

class ImageModelClass(models.Model):
    pic = models.ImageField(upload_to='myimage')
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'image_table'