# Generated by Django 3.2.11 on 2022-01-11 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0007_alter_article_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='questions',
        ),
        migrations.AddField(
            model_name='article',
            name='questions',
            field=models.TextField(blank=True),
        ),
    ]