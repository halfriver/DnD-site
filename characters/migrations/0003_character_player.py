# Generated by Django 3.0.5 on 2020-04-08 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0002_auto_20200407_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='player',
            field=models.BooleanField(null=True),
        ),
    ]
