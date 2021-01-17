from django.db import models

# Create your models here.


class Author(models.Model):
    """ Authors that have contributed to research articles. """

    first_name          = models.CharField(max_length=80)
    last_name           = models.CharField(max_length=80)
    url_link            = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f'{str(self.first_name)} {str(self.last_name)}'

class Article(models.Model):
    """ A research article.  """
    # Article types
    PUBLICATION = 'PU'
    REPORT = 'RP'
    OTHER = 'OT'
    ARTICLE_TYPE_CHOICES = [
        (PUBLICATION, 'Publication'),
        (REPORT, 'Report'),
        (OTHER, 'Other'),
    ]

    title =             models.CharField(max_length=200, default=None)
    description =       models.CharField(max_length=500, default=None)
    year_published =    models.CharField(max_length=5, default=None)
    article_type =      models.CharField(max_length=2,
                                         choices=ARTICLE_TYPE_CHOICES,
                                         default=OTHER)
    publisher =         models.CharField(max_length=200, blank=True)
    authors =           models.ManyToManyField(Author)
    file =              models.FileField(blank=True, null=True,
                                         upload_to='research/%Y/')
    link =              models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f'{self.title}, {self.year_published}, {[str(author) for author in self.authors.all()]}'






