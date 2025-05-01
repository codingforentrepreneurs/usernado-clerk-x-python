from django.conf import settings
from django.db import models

# Create your models here.

User = settings.AUTH_USER_MODEL

class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # user_obj.blogpost_set.all()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)