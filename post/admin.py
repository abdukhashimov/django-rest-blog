from django.contrib import admin

from post.models import Category, Tag, Post, Author


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Author)
