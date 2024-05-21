from django.db import models

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
