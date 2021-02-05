from django.db import models

from django.utils import timezone

# Create your models here.


class Author(models.Model):
    """ Authors that have contributed to research articles. """

    first_name          = models.CharField(max_length=80)
    last_name           = models.CharField(max_length=80)
    url_link            = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f'{str(self.first_name)} {str(self.last_name)}'

class PublishedManager(models.Manager):
    """ Custom manager that only returns published articles. """

    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Article(models.Model):
    """ A research article.  """
    objects = models.Manager()
    published = PublishedManager()

    ARTICLE_TYPE_CHOICES = [
        ('publication', 'Publication'),
        ('report', 'Report'),
        ('other', 'Other'),
    ]

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    title =             models.CharField(max_length=200, )
    description =       models.CharField(max_length=500, blank=True,)
    publish =           models.DateTimeField(default=timezone.now)          # When the article was posted to the website.
    date_published =    models.DateField(editable=True)                 # When the article was created.
    article_type =      models.CharField(max_length=12,
                                         choices=ARTICLE_TYPE_CHOICES,
                                         default='other')
    status =            models.CharField(max_length=12,
                                         choices=STATUS_CHOICES,
                                         default='draft')
    publisher =         models.CharField(max_length=200, blank=True)
    authors =           models.ManyToManyField(Author,)
    link =              models.URLField(max_length=1000, blank=True)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return f'{self.title}, {[str(author) for author in self.authors.all()]}'






