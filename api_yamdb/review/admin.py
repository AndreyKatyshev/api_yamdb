from django.contrib import admin

from .models import Comment, Review

class ReviewAdmin(admin.ModelAdmin):

    list_display = ('pk', 'text', 'pub_date', 'author', 'title')
    search_fields = ('text', 'author', 'title')
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


class CommentAdmin(admin.ModelAdmin):

    list_display = ('pk', 'text', 'created', 'author', 'review')
    search_fields = ('text', 'author', 'review')
    list_filter = ('created',)
    empty_value_display = '-пусто-'


admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)