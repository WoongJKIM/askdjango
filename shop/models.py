from django.db import models
from django.conf import settings
# Create your models here.

class Post(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL)
    title=models.CharField(max_length=100)