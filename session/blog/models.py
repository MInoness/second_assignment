from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 28)
    content = models.TextField()
    writer = models.CharField(max_length=20)
    createdAt = models.DateTimeField(auto_now_add=True)
    mail = models.CharField(max_length = 200)
    published_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.title