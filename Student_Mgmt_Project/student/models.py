from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
# Create your models here.

'''
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
'''

phone_regex = RegexValidator(
    regex=r"^\d{10}", message="phone must be 10 digits only"
)
CLASS_CHOICE = (
    ('CLASS ONE','CLASS ONE'),
    ('CLASS TWO','CLASS TWO'),
    ('CLASS THREE', 'CLASS THREE'),
    ('CLASS FOUR', 'CLASS FOUR'),
    ('CLASS FIVE','CLASS FIVE'),
    ('CLASS SIX','CLASS SIX'),
    ('CLASS SEVEN','CLASS SEVEN'),
    ('CLASS EIGHT','CLASS EIGHT'),
    ('CLASS NINE','CLASS NINE'),
    ('MATRIC','MATRIC')
)

class StudentUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)
    phone = models.CharField(unique=True, max_length=10, null=False, blank = False, validators=[phone_regex])
    date_of_birth = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='uploaded_img', blank=True)
    class_name = models.CharField(choices=CLASS_CHOICE, max_length=20)

    