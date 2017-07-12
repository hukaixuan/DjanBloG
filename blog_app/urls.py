from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^article/$', views.article, name='article'),
    url(r'^tag/$', views.tag, name='tag'),
    url(r'^archive/$', views.archive, name='archive'),
    url(r'^test/$', views.test, name='test'),
    url(r'^about/$', views.about, name='about')
]