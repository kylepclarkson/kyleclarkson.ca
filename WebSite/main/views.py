from django.shortcuts import render
from django.views.generic.base import TemplateView


def home(request):
    """ Return the homepage of the website. """
    return render(request, 'main/home.html')


class AboutView(TemplateView):

    template_name = 'main/about.html'

