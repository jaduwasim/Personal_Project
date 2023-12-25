from datetime import datetime, timedelta
import random
from django.conf import settings
from rest_framework import serializers
from account.models import UserModel
from account.utils import send_otp


class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(
        write_only =True,
        min_length = settings.MIN_PASSWORD_LENGTH,
        error_messages = {
            "min_length":f"Password Must be Longer than {settings.MIN_PASSWORD_LENGTH} Characters"
        }
    )
    class Meta:
        model = UserModel
        fields = (
            "phone_number",
            "email",
            "password1",
            "password2",
        )
    
    def validate(self, data):
        if data["password1"] != data["password2"]:
            raise serializers.ValidationError('Password do not match')
        return data
    
    def create(self, validate_data):
        otp = random.randint(1000, 9999)
        otp_expiry = datetime.now() + timedelta(minutes=10)
        user = UserModel(
            phone_number = validate_data["phone_number"],
            email = validate_data["email"],
            otp = otp,
            otp_expiry = otp_expiry,
            max_otp_try = settings.max_otp_try,
        )
        user.set_password(validate_data["password1"])
        user.save()
        send_otp(validate_data["phone_number"], otp)
        return user