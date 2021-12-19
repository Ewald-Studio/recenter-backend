from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .viewsets import *
from . import views

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


router = routers.DefaultRouter()
router.register('organizations', OrganizationViewSet, basename='organizations')
# router.register('userprofiles', UserProfileViewSet, basename='userprofiles')

urlpatterns = [
    path("/", include(router.urls)),
    path('login/', views.login, name="login"),
    path('userprofile/', views.userprofile, name="userprofile"),

    path('token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]