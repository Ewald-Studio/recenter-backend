# Generated by Django 3.2.11 on 2022-04-23 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgstructure', '0004_auto_20220111_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='contacts',
            field=models.TextField(blank=True),
        ),
    ]
