from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    images = models.ImageField(upload_to="images")
    content = models.TextField()

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name="comments")
    name = models.CharField(max_length=100)
    comm = models.TextField(null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.name