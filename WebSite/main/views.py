from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.core.mail import send_mail

from . import forms


def home(request):
    """ Return the homepage of the website. """
    comment_form = forms.CommentForm()

    print('Home called')

    if request.method == 'POST':
        if comment_form.is_valid():
            name = comment_form.cleaned_data['name']
            sender = comment_form.cleaned_data['email']
            message = comment_form.cleaned_data['message']

            send_mail(f'Email from {name}', message, sender, 'kyleclarkson17@hotmail.com')
            print('mail sent')
            return HttpResponseRedirect('/thanks/')

        else:
            print('Not valid')

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

