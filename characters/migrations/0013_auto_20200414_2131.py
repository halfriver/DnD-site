# Generated by Django 3.0.5 on 2020-04-15 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0012_auto_20200414_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='game_class',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='character',
            name='race',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
    ]
