from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.contrib import messages

from taggit.models import Tag

from .models import Post, Comment
from main.forms import CommentForm


def blog_list(request, tag_slug=None):
    """
    Get all published posts using tag_slug to filter result.
    """

    object_list = Post.published.all()
    tag = None
    if tag_slug:
        # use tag to filter results
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    POSTS_PER_PAGE = 8
    paginator = Paginator(object_list, POSTS_PER_PAGE)
    # The page the user is currently viewing.
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # Deliver first page
        posts = paginator.page(1)
    except EmptyPage:
        # Deliver last page
        posts = paginator.page(paginator.num_pages)

    context = {
        'page': page,
        'posts': posts,
        'tag': tag,
    }

    print('posts found: ', len(posts))

    return render(request,
                  'blog/blog_list.html',
                  context)


def blog_detail(request, year, month, day, post):
    """ Get specific post using slug. """
    # Issue: adding 'day' value when getting post makes post not found.
    post = get_object_or_404(Post,
                             slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,)

    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            name = comment_form.cleaned_data['name']
            sender = comment_form.cleaned_data['email']
            message = comment_form.cleaned_data['message']

            # create instance in database.
            Comment.objects.create(
                name=name,
                email=sender,
                message=message,
                post=post,
            )

            receivers = ['admin@email.com']
            if comment_form.cleaned_data['copy_sent']:
                receivers.append(sender)

            # send email
            send_mail(f'Comment by {name} on {post.title} - kyleclarkson.ca', message, sender, receivers)
            messages.add_message(request,
                                 messages.SUCCESS,
                                 'Thank you for your email!',
                                 extra_tags='bg-success text-white')

            # clear form
            comment_form = CommentForm()



    context = {
        'post': post,
        'comment_form': comment_form
    }

    return render(request,
                  'blog/blog_detail.html',
                  context)
