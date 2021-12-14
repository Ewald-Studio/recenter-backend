from django.db import models

from django.contrib.auth.models import User

class Organization(models.Model):
    name = models.CharField(max_length=255, blank=False)
    logo = models.ImageField(upload_to="logos")
    photo = models.ImageField(upload_to="photos")
    short_info = models.CharField(max_length=255, blank=True)
    main_phone = models.CharField(max_length=30, blank=True)
    description = models.TextField(blank=True)
    contacts = models.CharField(blank=True, max_length=255)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class UserProfile(models.Model):

    ROLES = (
        (1, "READER"),
        (2, "AUTHOR"),
        (3, "MODERATOR"),
        (4, "ADMIN"),
    )

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    fio = models.CharField(max_length=255, blank=True)
    profile_text = models.TextField(blank=True)
    position = models.CharField(max_length=255, blank=True)
    organization = models.ForeignKey(Organization, related_name="profiles", on_delete=models.CASCADE)
    role = models.CharField(max_length=1, choices=ROLES)

    def __str__(self):
        return self.fio