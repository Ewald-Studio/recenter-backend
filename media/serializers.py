from rest_framework import serializers
from media.models import (Article, ArticleFile, Comment, Question, Section)
from orgstructure.serializers import UserProfileSerializer

class CommentSerializer(serializers.ModelSerializer):
    author = UserProfileSerializer()

    class Meta:
        model = Comment
        fields = (
            'id',
            'author',
            'article',
            'datetime',
            'text',
            )


class ArticleSerializer(serializers.ModelSerializer):
    author = UserProfileSerializer()
    comments = CommentSerializer(many=True)

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
            'authorship',
            'author',
            'files',
            'sections',
            'questions',
            'status',
            'comments',
            )


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


