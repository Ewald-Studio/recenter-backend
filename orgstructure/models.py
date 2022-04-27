from django.db import models
from django.contrib.auth.models import User


class Organization(models.Model):
    name = models.CharField("Краткое наименование", max_length=255)
    logo = models.ImageField(upload_to="logos", blank=True, null=True)
    photo = models.ImageField(upload_to="photos", blank=True, null=True)
    short_info = models.CharField("Краткое описание (1 предложение)", max_length=255, blank=True)
    main_phone = models.CharField("Телефон", max_length=30, blank=True)
    description = models.TextField("Подробное описание", blank=True)
    contacts = models.TextField("Контактная информация", blank=True)
    website = models.CharField("Ссылка на сайт", max_length=255, blank=True)
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


class Feedback(models.Model):
    name = models.CharField("ФИО", max_length=255)
    email = models.EmailField("Электронная почта")
    specialist = models.CharField("Специалист", max_length=255, blank=True)
    message = models.TextField("Сообщение")
    created_at = models.DateTimeField(auto_now_add=True)
    is_new = models.BooleanField("Не отвечено (новое)", default=True)

    def __str__(self):
        if self.is_new:
            return f"(Новое) {self.name}"
        return self.name
