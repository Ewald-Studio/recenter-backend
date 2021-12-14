from django.contrib import admin

from .models import *

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(ArticleFile)
admin.site.register(Section)
admin.site.register(Question)