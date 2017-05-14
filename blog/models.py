from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.core.urlresolvers import reverse
from tagging.fields import TagField

# Create your models here.


class Post(models.Model):
    title = models.CharField('제목', max_length=50)
    slug = models.SlugField('별칭', unique=True, allow_unicode=True, help_text='별칭용 한단어')
    description = models.CharField('요약', max_length=100, blank=True, help_text='요약문장')
    content = models.TextField('내용')
    create_date = models.DateTimeField('생성일시', auto_now_add=True)
    modify_date = models.DateTimeField('수정일시', auto_now=True)
    tag = TagField()

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'my_post'
        ordering = ('-modify_date', )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,))

    def get_previous_post(self):
        return self.get_previous_by_modify_date()

    def get_next_post(self):
        return self.get_next_by_modify_date()