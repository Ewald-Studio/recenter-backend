from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from media.models import (Article, ArticleFile, Comment, Question, Section, ArticleFile)
from orgstructure.models import UserProfile
import datetime

from .serializers import (
    ArticleSerializer, 
    ArticleCreateOrUpdateSerializer,
    ArticleFileSerializer, 
    CommentSerializer, 
    QuestionSerializer, 
    SectionSerializer
)


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    
    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update':
            return ArticleCreateOrUpdateSerializer
        return super().get_serializer_class()

    @action(methods=['POST'], detail=True)
    def upload(self, request, pk):
        article = Article.objects.get(pk=pk)
        for file in request.FILES.getlist('files'):
            article_file, created = ArticleFile.objects.get_or_create(file=file)
            article_file.name = article_file.file.name.replace('.pdf', '').split('/')[-1]
            article_file.save()
            article.files.add(article_file)
        return Response({ 'success': True })

    def get_queryset(self):
        # role = self.request.query_params.get('role')
        user_pk = self.request.user.pk
        up = UserProfile.objects.get(user_id=user_pk)
        role = up.role
        if role == "WRITER":
            queryset = Article.objects.filter(author_id=self.request.user.pk).exclude(status="DELETED")
        elif role == "MODERATOR":
            queryset = Article.objects.filter(status="MODERATION")
        elif role == "ADMIN":
            queryset = Article.objects.all()

        return queryset

    def perform_create(self, serializer):
        if not self.request.user.is_anonymous:
            user = self.request.user
            writer = UserProfile.objects.get(user_id=user.id)
            serializer.save(author_id=writer.id)

        return False

class ArticleFileViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleFileSerializer
    queryset = ArticleFile.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        text = self.request.data["text"]
        article = self.request.data["article"]
        if not self.request.user.is_anonymous:
            user = self.request.user
            author = UserProfile.objects.get(user_id=user.id)
            serializer.save(article_id=article, author_id=author.id, text=text, datetime=datetime.datetime.now())
        


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class SectionViewSet(viewsets.ModelViewSet):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()

