from __future__ import unicode_literals   # for Python 2.X
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Bookmark(models.Model):
    title = models.CharField('사이트이름', max_length=100, blank=True, null=True)
    url = models.URLField('주소', unique=True)

    def __str__(self):
        return self.title
