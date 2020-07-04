from django.db import models
from django.conf import settings

# Create your models here.
class Radish(models.Model):
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField()
    lock = models.TextField()
    bell = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

class Article(models.Model):
    category = models.TextField()
    title = models.TextField()
    want = models.TextField()
    calling = models.TextField()
    soldout = models.BooleanField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)