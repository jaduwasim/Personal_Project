import datetime
import random
from django.conf import settings
from django.utils import timezone
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import viewsets
from .models import UserModel
from .serializers import UserSerializer
from account.utils import send_otp

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    
    @action(detail=True, methods='PATCH')
    def verify_otp(self, request, pk=None):
        instance = self.get_object()
        if (
            not instance.is_active
            and instance.ot == request.data.get("otp")
            and instance.otp_expiry
            and timezone.now() < instance.otp_expiry
        ):
            instance.is_active =True
            instance.otp_expiry = None
            instance.max_otp_expiry = settings.MAX_OTP_TRY
            instance.otp_max_out = None
            instance.save()
            return Response(
                "Succesfully Verifed the User", status=status.HTTP_200_OK
            )
        return Response(
            "User Active or Please Enter Correct OTP", status=status.HTTP_400_BAD_REQUEST
        )

    @action(detail=True, methods=['PATCH'])
    def regenerate_otp(self, request, pk=None):
        instance = self.get_object()

        if int(instance.max_otp_expiry) == 0 and timezone.now() < instance.otp_max_out:
            return Response(
                "Max OTP try reached, try after 10 minute ",
                status=status.HTTP_400_BAD_REQUEST
            )
        otp = random.randint(1000,9999)
        otp_expiry = timezone.now() + datetime.timedelta(minutes=10)
        max_otp_try = int(instance.max_otp_expiry) -1

        instance.otp = otp
        instance.otp_expiry = otp_expiry
        instance.max_otp_expiry = max_otp_try

        if max_otp_try == 0:
            instance.otp_max_out = timezone.now() + datetime.timedelta(minutes=10)
        elif max_otp_try == -1:
            instance.max_otp_try = settings.MAX_OTP_TRY
        else:
            instance.otp_max_out = None
            instance.max_otp_try = max_otp_try
        instance.save()
        send_otp(instance.phone_number, otp)
        return Response("Success New Generate OTP", status=status.HTTP_200_OK)
