from django.contrib import admin
from .models import *


class ArticleAdmin(admin.ModelAdmin):

    exclude = ('date_publish', )


# Register your models here.
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
