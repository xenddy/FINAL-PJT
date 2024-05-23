from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()


class Article(models.Model):
    CATEGORY_CHOICES = [
        ('Travel', 'Travel'),
        ('Camping', 'Camping'),
        ('Leisure', 'Leisure'),
        ('Cooking', 'Cooking'),
    ]
    
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    Article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments"
    )
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.content
        

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('user', 'article')