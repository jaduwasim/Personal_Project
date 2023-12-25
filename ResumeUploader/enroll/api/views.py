from rest_framework.viewsets import ModelViewSet
from enroll.api.serialziers import ProfileSerialzier
from enroll.models import Profile

class ProfileAPI(ModelViewSet):
    serializer_class = ProfileSerialzier
    queryset = Profile.objects.all()