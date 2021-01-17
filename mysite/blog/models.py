from django.db import models

from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    ''' Blog Post'''

    title =             models.CharField(max_length=255)
    body =              RichTextField(blank=True, null=True)
    snippet =           models.CharField(max_length=200)
    date_created =      models.DateTimeField(auto_now=True)
    date_modified =     models.DateTimeField(auto_now_add=True)

    def __str__(self):
        send = self.title + ' created on ' + str(self.date_created)
        if str(self.date_modified) != str(self.date_created) :
            send += ' modified ' + str(self.date_modified)
        return send
