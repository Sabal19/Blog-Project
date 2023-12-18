from django.urls import path
from . import views

urlpatterns= [
    path('',views.index,name='index'),
    path('getposts',views.getposts),
    path('blogs',views.blogs,name='blogs'),
    path('logout',views.logout,name='logout'),
    path('postdetail/<str:pk>',views.postdetail,name='postdetail'),
    path('category/<str:cat>', views.getpostbycategory, name='category'),
    path('userprofile', views.userprofile, name='userprofile'),
    path('updateprofile/<str:pk>', views.updateprofile, name='updateprofile'),
    path('deleteprofile', views.deleteprofile, name='deleteprofile'),
    path('myblogs', views.myblogs, name='myblogs'),
    path('deleteblogs/<str:pk>', views.deleteblogs, name='deleteblogs'),
    path('editblogs/<str:pk>', views.editblogs, name='editblogs'),

]