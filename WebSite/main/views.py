from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.core.mail import send_mail
from django.contrib import messages

from .forms import CommentForm
from blog.models import Comment


def home(request):
    """ Return the homepage of the website. """

    print('Home called')
    if request.method == 'POST':
        # user has submitted a comment.
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            name = comment_form.cleaned_data['name']
            sender = comment_form.cleaned_data['email']
            message = comment_form.cleaned_data['message']

            # create instance in database.
            Comment.objects.create(
                name=name,
                email=sender,
                message=message
            )

            # send email
            send_mail(f'Website email - general from {name}', message, sender, ['kyleclarkson17@hotmail.com',])
            messages.add_message(request,
                                 messages.SUCCESS,
                                 'Thank you for your email!',
                                 extra_tags='bg-success text-white')
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

