from django.db import models
from django.contrib.auth.models import User


class Organization(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="logos", blank=True, null=True)
    photo = models.ImageField(upload_to="photos", blank=True, null=True)
    short_info = models.CharField(max_length=255, blank=True)
    main_phone = models.CharField(max_length=30, blank=True)
    description = models.TextField(blank=True)
    contacts = models.TextField(blank=True)
    website = models.CharField(max_length=255, blank=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class UserProfile(models.Model):

    ROLES = (
        ("READER", "Читатель"),
        ("WRITER", "Автор"),
        ("MODERATOR", "Модератор"),
        ("ADMIN", "Администратор"),
    )

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    fio = models.CharField(max_length=255, blank=True)
    profile_text = models.TextField(blank=True)
    position = models.CharField(max_length=255, blank=True)
    organization = models.ForeignKey(Organization, related_name="profiles", on_delete=models.CASCADE)
    role = models.CharField(max_length=9, choices=ROLES)

    def __str__(self):
        return self.fio