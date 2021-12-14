from rest_framework import viewsets, mixins
from media.models import (Article, ArticleFile, Comment, Question, Section)


from .serializers import (
    ArticleSerializer, 
    ArticleFileSerializer, 
    CommentSerializer, 
    QuestionSerializer, 
    SectionSerializer
)


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


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

