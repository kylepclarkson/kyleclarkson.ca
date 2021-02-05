from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Article

# Create your views here.


def research_list(request):
    """ Get research publication and articles, sorted by date. """

    object_list = Article.published.all()
    # publication_posts = object_list.filter(article_type__equal='publication')
    # report_post = object_list.filter(article_type__equal = 'report')

    context = {
        'posts': object_list
    }

    return render(request,
                  'research/article_list.html',
                  context)






