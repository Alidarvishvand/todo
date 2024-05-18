from django.db import models
from accounts.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    status = models.BooleanField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()
    
    def __str__(self):
        return self.title
    