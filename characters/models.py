from django.db import models

STATUS = (('alive', 'Alive'),('deceased','Deceased'),('unknown','Unknown'))

class Character(models.Model):
    prename = models.CharField(max_length=30, blank=True, default="")
    name = models.CharField(max_length=30, unique=True)
    postname = models.CharField(max_length=30, blank=True, default="")
    player = models.BooleanField(null=True)
    status = models.CharField(max_length=10, choices=STATUS, default='unknown')
    portrait = models.ImageField(upload_to='character_portraits', null=True)
    description = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    strength = models.IntegerField(blank=True, null=True)
    dexterity = models.IntegerField(blank=True, null=True)
    constitution = models.IntegerField(blank=True, null=True)
    intelligence = models.IntegerField(blank=True, null=True)
    wisdom = models.IntegerField(blank=True, null=True)
    charisma = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
