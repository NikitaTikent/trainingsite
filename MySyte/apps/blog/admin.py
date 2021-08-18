from django.contrib import admin
from .models import Blog_articles, Blog_comments

admin.site.register(Blog_articles)
admin.site.register(Blog_comments)
