from rest_framework import viewsets, mixins
from orgstructure.models import (Organization, UserProfile)


from .serializers import (
    OrganizationSerializer, 
    OrganizationSaveSerializer,
    UserProfileSerializer
)


class OrganizationViewSet(viewsets.ModelViewSet):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
            return OrganizationSaveSerializer
        return super().get_serializer_class()


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
