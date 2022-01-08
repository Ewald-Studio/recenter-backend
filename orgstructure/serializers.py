from rest_framework import serializers
from orgstructure.models import (Organization, UserProfile)


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer()

    class Meta:
        model = UserProfile
        fields = '__all__'
