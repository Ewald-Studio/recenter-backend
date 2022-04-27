from django.shortcuts import render
import json
from django.http import JsonResponse
from .models import *
from django.contrib.auth import authenticate

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


def login(request):
    data = json.loads(request.body)
    username = data["username"]
    password = data["password"]

    user = authenticate(username=username, password=password)

    if user is not None:
        refresh_token = RefreshToken.for_user(user)
        response = {
            'refresh': str(refresh_token),
            'access': str(refresh_token.access_token),
        }
        return JsonResponse(response)        
    else:
        error = {
            "code": "INVALID_USER_LOGIN_OR_PASSWORD",
            "detail": "Combination of given user and password is invalid",
        }
        return JsonResponse(error, status=403)


@api_view()
def userprofile(request):
    up = UserProfile.objects.get(user_id=request.user.pk)
    profile = {
        "user_id": request.user.pk,
        "profile_id": up.id,
        "fio": up.fio,
        "profile_text": up.profile_text,
        "position": up.position,
        "role": up.role,
    }
    if up.organization_id:
        organization = Organization.objects.get(id=up.organization_id)
        organization_dict = {
            "id": organization.id,
            "name": organization.name,
            "is_staff": organization.is_staff,
        }
        profile["organization"] = organization_dict
    
    return Response(profile)