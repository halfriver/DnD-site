# Generated by Django 3.0.5 on 2020-04-15 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0010_auto_20200409_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='game_class',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='character',
            name='race',
            field=models.TextField(blank=True, default=''),
        ),
    ]