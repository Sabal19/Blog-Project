from django.contrib import admin
from .models import Blog,Category,Author

# Register your models here.
class Blogdetail(admin.ModelAdmin):
    list_display=['author','title','content','image','views']

admin.site.register(Blog,Blogdetail)
admin.site.register(Category)
admin.site.register(Author)