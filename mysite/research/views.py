from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Article, Author

# Create your views here.


class ResearchIndex(ListView):
    """ Get research publication and articles, sorted by date. """
    model = Article
    template_name = 'research/article.html'
    ordering = ['-id'] # TODO Change to date published.

class ResearchPostDetail(DetailView):

    model = Article
    template_name = 'research/article_detail.html'
    pass