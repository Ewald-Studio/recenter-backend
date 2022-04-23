from django.contrib import admin
from django.urls import path, include

from media import urls as media_api
from orgstructure import urls as orgstructure_api
from web import urls as web_urls

urlpatterns = [
    path('django-admin/', admin.site.urls),
    path('api/media/', include(media_api)),
    path('api/orgstructure/', include(orgstructure_api)),
    path('', include(web_urls)),
]
