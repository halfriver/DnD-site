# Generated by Django 3.0.5 on 2020-04-09 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0006_character_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='portrait',
            field=models.ImageField(null=True, upload_to='media/character_portraits'),
        ),
    ]
