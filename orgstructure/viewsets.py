from rest_framework import viewsets, mixins
from orgstructure.models import (Organization, UserProfile)


from .serializers import (
    OrganizationSerializer, 
    UserProfileSerializer
)


class OrganizationViewSet(viewsets.ModelViewSet):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
