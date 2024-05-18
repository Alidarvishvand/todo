from django.db import models
from accounts.models import User
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=150)
    content = models.TextField()
    status = models.BooleanField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()
    
    def __str__(self):
        return self.title
    
    
