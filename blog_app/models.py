from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField('头像', upload_to='avatar/%Y/%m', \
                                default='avatar/default.png', max_length=200, blank=True, null=True)
    url = models.URLField(max_length=100, blank=True, null=True, verbose_name='个人网页地址')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.username


# Create your models here.
class Tag(models.Model):
    name = models.CharField('标签名称', max_length=30)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField('分类', max_length=30)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ArticleManager(models.Manager):
    def distinct_date(self):
        distinct_date_list = []
        date_list = self.values('date_publish')
        for date in date_list:
            date = date['date_publish'].strftime('%Y /%m 文章存档')
            if date not in distinct_date_list:
                distinct_date_list.append(date)
        return distinct_date_list


class Article(models.Model):
    title = models.CharField('文章标题', max_length=50)
    desc = models.CharField('文章描述', max_length=50)
    content = models.TextField('文章内容')
    click_count = models.IntegerField('点击次数', default=0)
    is_recommend = models.BooleanField('是否推荐', default=False)
    date_publish = models.DateTimeField('发布时间', auto_now_add=True)
    user = models.ForeignKey(User, verbose_name='作者')
    category = models.ForeignKey(Category, blank=True, null=True, verbose_name='分类')
    tag = models.ManyToManyField(Tag, verbose_name='标签')

    objects = ArticleManager()

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField('评论内容')
    username = models.CharField('用户名', max_length=30, blank=True, null=True)
    email = models.EmailField('邮箱地址', max_length=50, blank=True, null=True)
    url = models.URLField('个人网址', max_length=100, blank=True, null=True)
    date_publish = models.DateTimeField('发布时间', auto_now_add=True)
    user = models.ForeignKey(User, blank=True, null=True, verbose_name='用户')
    article = models.ForeignKey(Article, blank=True, null=True, verbose_name='文章')
    pid = models.ForeignKey('self', blank=True, null=True, verbose_name='文章')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.id)









