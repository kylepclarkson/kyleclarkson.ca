from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from taggit.models import Tag

from .models import Post
# Create your views here.


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
    print(f'post_detail called')
    print(f'post: {post}')
    post = get_object_or_404(Post,
                             slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    context = {
        'post': post
    }

    return render(request,
                  'blog/blog_detail.html',
                  context)
