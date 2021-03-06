# Generated by Django 3.0.5 on 2020-04-08 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='charisma',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='constitution',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='dexterity',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='intelligence',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='character',
            name='strength',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='wisdom',
            field=models.IntegerField(null=True),
        ),
    ]
