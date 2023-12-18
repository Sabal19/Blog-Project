from django.contrib import admin
from . models import User


# Register your models here.

class Admindetail(admin.ModelAdmin):
    list_display=['id','email']
admin.site.register(User,Admindetail)