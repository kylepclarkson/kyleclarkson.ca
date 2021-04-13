from django.shortcuts import render
from django.views.generic.base import TemplateView


def home(request):
    """ Return the homepage of the website. """
    return render(request, 'main/home.html')


class AboutView(TemplateView):
    """ Return the about page. """
    template_name = 'main/about.html'


class ProjectsView(TemplateView):
    """ Return the about page. """
    template_name = 'main/projects.html'


class ResearchView(TemplateView):
    """ Return the about page. """
    template_name = 'main/research.html'

