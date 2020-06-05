from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')
    nickname = models.CharField(max_length=30, default='익명')

    def __str__(self):
        return self.username

class Villagers(models.Model):
    kr_name = models.CharField(max_length=10)
    jp_name = models.CharField(max_length=10)
    en_name = models.CharField(max_length=10)
    sex = models.CharField(max_length=10)
    birthday = models.TextField()
    character = models.TextField()
    species = models.CharField(max_length=10)
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_villager')
    live_with = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='live_villager')

    def __str__(self):
        return self.kr_name

class Bug(models.Model):
    name = models.CharField(max_length=20)
    date = models.TextField()
    time = models.TextField()
    where = models.TextField()
    bell = models.IntegerField()
    catch_user = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='catch_bug')

    def __str__(self):
        return self.name

class Fish(models.Model):
    name = models.CharField(max_length=20)
    date = models.TextField()
    time = models.TextField()
    where = models.TextField()
    size = models.TextField()
    bell = models.IntegerField()
    catch_user = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='catch_fish')

    def __str__(self):
        return self.name