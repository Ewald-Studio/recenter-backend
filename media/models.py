from django.db import models
from django.dispatch import receiver
import os.path

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

    title = models.CharField(max_length=255, blank=True)
    annotation = models.TextField(blank=True)
    text = models.TextField(blank=True)
    photo = models.ImageField(upload_to="article_photo", blank=True, null=True)
    video = models.CharField(max_length=255, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_edit_date = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    authorship = models.CharField(max_length=255, blank=True, null=True)
    author = models.ForeignKey(UserProfile, related_name="articles", on_delete=models.SET_NULL, blank=True, null=True)
    files = models.ManyToManyField(ArticleFile, related_name="articles", blank=True)
    sections = models.ManyToManyField(Section, related_name="articles", blank=True)
    questions = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUSES, default="NEW")
    is_important = models.BooleanField(default=False)

    @property
    def video_full_path(self):
        if "watch" in self.video:
            return self.video.replace('watch?v=', 'embed/')
        if 'youtu.be' in self.video:
            return self.video.replace('youtu.be/', 'youtube.com/embed/')


class Comment(models.Model):
    article = models.ForeignKey(Article, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, related_name="comments", on_delete=models.SET_NULL, null=True)
    text = models.TextField(blank=False)
    datetime = models.DateTimeField(auto_now_add=True)


@receiver(models.signals.post_delete, sender=ArticleFile)
def auto_delete_on_delete(sender, instance, **kwargs):
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)


