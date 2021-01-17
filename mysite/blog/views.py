from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post

# Create your views here.

class BlogIndex(ListView):
    model = Post
    template_name = 'blog/blog.html'
    ordering = ['-id']


class BlogPostDetail(DetailView):

    model = Post
    template_name = 'blog/blog_detail.html'


