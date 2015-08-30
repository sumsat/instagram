from __future__ import absolute_import

from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
        list_display = ('slug',
                        'caption',
                        'author',
                        'date_created',
                        'date_updated', )

admin.site.register(Post, PostAdmin)
