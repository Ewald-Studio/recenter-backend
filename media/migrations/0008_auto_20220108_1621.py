# Generated by Django 3.2.11 on 2022-01-08 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0007_alter_article_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='files',
        ),
        migrations.AddField(
            model_name='articlefile',
            name='article',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='media.article'),
            preserve_default=False,
        ),
    ]