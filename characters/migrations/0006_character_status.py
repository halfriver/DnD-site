# Generated by Django 3.0.5 on 2020-04-09 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0005_auto_20200408_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='status',
            field=models.CharField(choices=[('alive', 'Alive'), ('deceased', 'Deceased'), ('unknown', 'Unknown')], default='unknown', max_length=10),
        ),
    ]
