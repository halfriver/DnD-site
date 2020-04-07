from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=30, unique=True)
    portrait = models.ImageField(upload_to='character_portraits', null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
