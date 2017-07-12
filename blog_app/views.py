import logging
from django.shortcuts import render
from django.conf import settings
from .models import *
from .forms import *


# 日志的使用
logger = logging.getLogger('blog_app.views')
# try:
#     pass
# except Exception as e:
#     logger.error(e)


def global_setting(request):
    return {
            'SITE_NAME': settings.SITE_NAME,
    }


def index(request):
    article_list = Article.objects.all()
    return render(request, 'index.html', locals())


def article(request):
    try:
        # 获取文章id
        id = request.GET.get('id', None)
        try:
            # 获取文章信息
            article = Article.objects.get(pk=id)
        except Article.DoesNotExist:
            return render(request, '404.html', {'reason': '没有找到对应的文章'})

        # 评论表单
        comment_form = CommentForm({'author': request.user.username,
                                    'email': request.user.email,
                                    'url': request.user.url,
                                    'article': id} if request.user.is_authenticated() else{'article': id})
        # 获取评论信息
        comments = Comment.objects.filter(article=article).order_by('id')
        comment_list = []
        for comment in comments:
            for item in comment_list:
                if not hasattr(item, 'children_comment'):
                    setattr(item, 'children_comment', [])
                if comment.pid == item:
                    item.children_comment.append(comment)
                    break
            if comment.pid is None:
                comment_list.append(comment)
    except Exception as e:
        print(e)
        logger.error(e)
    return render(request, 'article.html', locals())


def tag(request):
    tag_list = Tag.objects.all()
    return render(request, 'tag.html', locals())


def archive(request):
    try:
        # year = request.GET.get('year', None)
        # month = request.GET.get('month', None)
        # article_list = Article.objects.filter(date_publish__contains=year+'-'+month)
        # article_list = getPage(request, article_list)
        article_list = Article.objects.all()
    except Exception as e:
        logger.error(e)
    return render(request, 'archive.html', locals())

def about(request):
    return render(request, 'about.html')


def test(request):
    print(locals())
    return render(request, 'test.html', locals())
