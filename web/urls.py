from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sections/<int:section_id>/", views.article_list, name="article_list"),
    path("articles/<int:article_id>/", views.article_item, name="article_item"),
    path("search/", views.article_search, name="article_search"),
    path("organizations/", views.organization_list, name="organization_list"),
    path("organizations/<int:organization_id>/", views.organization_item, name="organization_item"),
]