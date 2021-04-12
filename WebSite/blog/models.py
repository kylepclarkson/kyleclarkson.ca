from django.db import models
from django.utils import timezone
from django.urls import reverse

from taggit.managers import TaggableManager
from ckeditor_uploader import fields


class PublishedManager(models.Manager):
    """ Custom manager that only returns published posts. """

    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    """ A blog post with with taggit tags and ckeditor text body field. """

    # set query managers.
    objects = models.Manager()
    published = PublishedManager()

    # A post can either be in a state of draft or published.
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    title = models.CharField(max_length=400)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    excerpt = models.TextField() # sort bit describing article.
    image = models.ImageField(upload_to='blog/%Y/%m/%d', default='no_image.png')
    body = fields.RichTextUploadingField(blank=True, null=True)
    publish = models.DateTimeField(default=timezone.now)  # when post was published.
    created = models.DateTimeField(auto_now_add=True)  # when the post was first created.
    updated = models.DateTimeField(auto_now=True)  # when the post was last updated.
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    tags = TaggableManager()  # Tags associated with posts.

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return f'{self.title}, {self.status}'

    def get_absolute_url(self):
        return reverse('blog:blog-detail',
                       args=[self.publish.year, self.publish.month, self.publish.day, self.slug])
