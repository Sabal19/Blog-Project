from django.test import TestCase
from django.db import models
from datetime import datetime
# Create your tests here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=10000)
    createdat = models.DateTimeField(default=datetime.now, blank=True)
    