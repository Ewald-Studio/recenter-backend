from django.contrib import admin
from django.urls import path, include

from media import urls as media_api
from media import urls as orgstructure_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('media/', include(media_api)),
    path('orgstructure/', include(orgstructure_api)),
]
