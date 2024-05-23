from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType



class CommonFields(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        abstract = True

    def __str__(self):
        return self.title

class Travel(CommonFields):
    pass

class Camping(CommonFields):
    pass

class Leisure(CommonFields):
    pass

class Cooking(CommonFields):
    pass

class Comments(models.Model):
    content = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    object_id = models.PositiveIntegerField()


    def __str__(self):
        return self.content