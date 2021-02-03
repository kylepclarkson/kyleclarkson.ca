from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('',  views.BlogIndex.as_view(), name='blog-index'),
    path('blog_detail/<int:pk>/', views.BlogPostDetail.as_view(), name='blog-detail'),

]
