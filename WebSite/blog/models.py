from django.db import models
from django.utils import timezone
from django.urls import reverse

# from taggit.managers import TaggableManager
#
# from ckeditor.fields import RichTextField


class PublishedManager(models.Manager):
    """ Custom manager that only returns published posts. """

    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    """ Blog post """

    # set query managers.
    objects = models.Manager()  # default
    published = PublishedManager()

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    title =         models.CharField(max_length=255)
    slug =          models.SlugField(max_length=250, unique_for_date='publish')
    # body =          RichTextField(blank=True, null=True)
    publish =       models.DateTimeField(default=timezone.now)      # when post was published.
    created =       models.DateTimeField(auto_now_add=True)         # when the post was first created.
    updated =       models.DateTimeField(auto_now=True)             # when the post was last updated.
    status =        models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    # tags =          TaggableManager()   # Tags associated with posts.

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return f'{self.title}, {self.status}'

    def get_absolute_url(self):
        return reverse('blog:blog-detail',
                       args=[self.publish.year, self.publish.month, self.publish.day, self.slug])


