from django.db import models
from django.conf import settings
# Create your models here.
class design(models.Model):
    title = models.CharField(max_length=100)
    design_img = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=10)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)