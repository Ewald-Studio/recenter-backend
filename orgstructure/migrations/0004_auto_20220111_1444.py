# Generated by Django 3.2.11 on 2022-01-11 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgstructure', '0003_auto_20220107_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='logos'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
    ]
