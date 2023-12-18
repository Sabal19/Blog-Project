from django.db import models
from datetime import datetime
# from django.contrib.auth.models import User
from django.conf import settings
from account.models import User

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
    
    name = models.CharField(max_length=100, unique=True,null=True,blank=True)
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    image = models.ImageField(upload_to='author/',blank= True, null=True)
    def __str__(self):
        return self.name
    

class Blog(models.Model):
    title = models.CharField(max_length=100,blank=True)
    # author = models.CharField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    author = models.ForeignKey(User,on_delete=models.CASCADE, blank=True,null=True)
    content = models.CharField(max_length=10000,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts',null=True,blank=True)
    image = models.ImageField(upload_to='blogpic/',blank=True)
    views = models.IntegerField(null=True,blank=True)
    likes = models.IntegerField(null=True,blank=True)
    is_feature = models.BooleanField(default=False,blank=True)

    def __str__(self):
        return self.title



    