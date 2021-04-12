from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    # all blog posts
    path('', views.blog_list, name='blog_list'),
    # specific blog post
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.blog_detail, name='blog-detail'),
    # blog posts belonging to a tag.
    path('tag/<slug:tag_slug>/', views.blog_list, name='blog-list-by-tag'),
]
