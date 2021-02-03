from django.db import models
from django.utils import timezone
from django.urls import reverse

from taggit.managers import TaggableManager

from ckeditor.fields import RichTextField


class PublishManager(models.Manager):
    """ Custom manager that only returns published posts. """

    def get_queryset(self):
        return super(PublishManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    """ Blog post """

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    title =         models.CharField(max_length=255)
    slug =          models.SlugField(max_length=250, unique_for_date='publish')
    body =          RichTextField(blank=True, null=True)
    publish =       models.DateTimeField(default=timezone.now)      # when post was published.
    created =       models.DateTimeField(auto_now_add=True)         # when the post was first created.
    updated =       models.DateTimeField(auto_now=True)             # when the post was last updated.
    status =        models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    tags =          TaggableManager()   # Tags associated with posts.

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return f'{self.title}, {self.publish}'

    def get_absolute_url(self):
        # TODO
        return reverse('')