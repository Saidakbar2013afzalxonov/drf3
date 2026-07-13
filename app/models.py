from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(blank=False, null=False)
    body = models.TextField()
    user = models.CharField(max_length=50, blank=False, null = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title
