from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .viewsets import *

router = routers.DefaultRouter()
router.register('organizations', OrganizationViewSet, basename='organizations')
router.register('userprofiles', UserProfileViewSet, basename='userprofiles')

urlpatterns = [
    path("/", include(router.urls)),
]