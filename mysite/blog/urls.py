from django.urls import path

from .views import *

urlpatterns = [
    path('',  BlogIndex.as_view(), name='blog-index'),
    path('blog_detail/<int:pk>/', BlogPostDetail.as_view(), name='blog-detail'),

]
app_name = 'blog'
