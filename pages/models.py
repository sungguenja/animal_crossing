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