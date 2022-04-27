from rest_framework import serializers
from orgstructure.models import (Organization, UserProfile)


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class OrganizationSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('name', 'short_info', 'main_phone', 'description', 'contacts', 'website',)


class UserProfileSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer(required=False)

    class Meta:
        model = UserProfile
        fields = '__all__'
