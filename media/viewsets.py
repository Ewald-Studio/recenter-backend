from django.http import request
from rest_framework import viewsets, mixins
from media.models import (Article, ArticleFile, Comment, Question, Section)
from orgstructure.models import UserProfile


from .serializers import (
    ArticleSerializer, 
    ArticleFileSerializer, 
    CommentSerializer, 
    QuestionSerializer, 
    SectionSerializer
)


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    
    def get_queryset(self):
        # role = self.request.query_params.get('role')
        user_pk = self.request.user.pk
        up = UserProfile.objects.get(user_id=user_pk)
        role = up.role
        if role == "WRITER":
            queryset = Article.objects.filter(author_id=self.request.user.pk)
        elif role == "MODERATOR":
            queryset = Article.objects.filter(status="MODERATION")
        elif role == "ADMIN":
            queryset = Article.objects.all()

        return queryset


class ArticleFileViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleFileSerializer
    queryset = ArticleFile.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class SectionViewSet(viewsets.ModelViewSet):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()

