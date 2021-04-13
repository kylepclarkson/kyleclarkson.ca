from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.core.mail import send_mail

from .forms import CommentForm


def home(request):
    """ Return the homepage of the website. """

    print('Home called')

    if request.method == 'POST':
        comment_form = CommentForm(request)
        if comment_form.is_valid():
            name = comment_form.cleaned_data['name']
            sender = comment_form.cleaned_data['email']
            message = comment_form.cleaned_data['message']

            send_mail(f'Email from {name}', message, sender, 'kyleclarkson17@hotmail.com')
            print('mail sent')

        else:
            print('Not valid')
    else:
        comment_form = CommentForm()

    context = {
        'name': 'Hello',
        'comment_form': comment_form
    }
    print('Context:', context)

    return render(request, 'main/home.html', context=context)


class AboutView(TemplateView):
    """ Return the about page. """
    template_name = 'main/about.html'


class ProjectsView(TemplateView):
    """ Return the about page. """
    template_name = 'main/projects.html'


class ResearchView(TemplateView):
    """ Return the about page. """
    template_name = 'main/research.html'

