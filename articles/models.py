from django.db import models
from django.contrib.auth.models import User
import os
from django.conf import settings

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # add in Auther alter
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE,)
    # add in thumbnali later
    thumb = models.FileField("uploads/", blank=True)


    # in ""Article.objects.all()""  outputs ==>  ""<QuerySet [<Article: Article object (1)>]>""
    # to make it easy to see we change the __str__ func
    # this function returns the str of this hole objec as ""nameofobject object"" so we change it

    def __str__(self):

        return self.title if self.title else self.body if self.body else self.slug if self.slug else str(self.date)

    def snippet(self):
        return self.body if len(self.body) < 20 else self.body[:20] + " • • •"
    
    def thumb_delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.thumb.name))

# this makes the file witch contains these upper things in a nice format
    # python manage.py makemigrations       prep of migration
# this migrates that file to database
    # python manage.py migrate              doing migration to db
