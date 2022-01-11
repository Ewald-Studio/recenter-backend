from rest_framework import serializers
from media.models import (Article, ArticleFile, Comment, Question, Section)
from orgstructure.serializers import UserProfileSerializer

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ArticleFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleFile
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'


class ArticleCreateOrUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'annotation',
            'text',
            'photo',
            'video',
            'publish_date',
            'authorship',
            'sections',
            'questions',
            'status',
        )

class ArticleSerializer(serializers.ModelSerializer):
    author = UserProfileSerializer(required=False)
    comments = CommentSerializer(required=False, many=True)
    files = ArticleFileSerializer(required=False, many=True)

    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'annotation',
            'text',
            'photo',
            'video',
            'creation_date',
            'publish_date',
            'last_edit_date',
            'authorship',
            'author',
            'files',
            'sections',
            'questions',
            'status',
            'comments',
        )
