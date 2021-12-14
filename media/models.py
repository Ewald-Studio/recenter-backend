from django.db import models

from orgstructure.models import UserProfile


class Question(models.Model):
    text = models.CharField(max_length=255, blank=False)


class Section(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)


class ArticleFile(models.Model):
    name = models.CharField(max_length=255, blank=False)
    file = models.FileField(upload_to="files")


class Article(models.Model):

    STATUSES = (
        ("NEW", "Новый"),
        ("MODERATION", "На модерации"),
        ("REJECTED", "Отклонено"),
        ("APPROVED", "Опубликовано"),
        ("DELETED", "Удалено"),
    )

    title = models.CharField(max_length=255, blank=False)
    annotation = models.TextField(blank=True)
    text = models.TextField(blank=True)
    photo = models.ImageField(upload_to="article_photo")
    video = models.CharField(max_length=255, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateTimeField()
    authorship = models.CharField(max_length=255, blank=False)
    author = models.ForeignKey(UserProfile, related_name="articles", on_delete=models.SET_NULL, null=True)
    files = models.ManyToManyField(ArticleFile, related_name="articles")
    sections = models.ManyToManyField(Section, related_name="articles")
    questions = models.ManyToManyField(Question, related_name="articles")
    status = models.CharField(max_length=10, choices=STATUSES)


class Comment(models.Model):
    article = models.ForeignKey(Article, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, related_name="comments", on_delete=models.SET_NULL, null=True)
    text = models.TextField(blank=False)
    datetime = models.DateTimeField(auto_now_add=True)