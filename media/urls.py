from django.urls import path, re_path
from django.conf.urls import include
from rest_framework import routers
from .viewsets import *

router = routers.DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')
router.register('articlefiles', ArticleFileViewSet, basename='articlefiles')
router.register('comments', CommentViewSet, basename='comments')
router.register('questions', QuestionViewSet, basename='questions')
router.register('sections', SectionViewSet, basename='sections')

urlpatterns = [
    re_path(r'^', include(router.urls)),
]