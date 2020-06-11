from django.db import models
from django.conf import settings
# Create your models here.
class design(models.Model):
    title = models.CharField(max_length=100)
    design_img = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=10)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_design')

    def __str__(self):
        return '{0}, {1}, {2}'.format(self.title, self.category, self.user)

class artwork(models.Model):
    title = models.CharField(max_length=100)
    original = models.CharField(max_length=100)
    fake = models.BooleanField()
    have_user = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='have_artwork')

    def __str__(self):
        return self.title

class fossil_category(models.Model):
    title = models.CharField(max_length=100)
    tmi = models.TextField()

    def __str__(self):
        return self.title

class fossil(models.Model):
    category = models.ForeignKey(fossil_category,on_delete=models.CASCADE)
    part = models.CharField(max_length=100)
    bell = models.IntegerField()
    have_user = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='have_fossil')
    
    def __str__(self):
        return '{0}의 {1}'.format(self.category,self.part)
    
class song(models.Model):
    kr_title = models.CharField(max_length=100)
    jp_title = models.CharField(max_length=100)
    en_title = models.CharField(max_length=100)

    def __str__(self):
        return self.kr_title