from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=30, unique=True)
    portrait = models.ImageField(upload_to='character_portraits', null=True)
    description = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    strength = models.IntegerField(null=True)
    dexterity = models.IntegerField(null=True)
    constitution = models.IntegerField(null=True)
    intelligence = models.IntegerField(null=True)
    wisdom = models.IntegerField(null=True)
    charisma = models.IntegerField(null=True)

    def __str__(self):
        return self.name
