# Generated by Django 3.2.11 on 2022-01-08 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0008_auto_20220108_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlefile',
            name='article',
        ),
        migrations.AddField(
            model_name='article',
            name='files',
            field=models.ManyToManyField(blank=True, related_name='articles', to='media.ArticleFile'),
        ),
    ]
