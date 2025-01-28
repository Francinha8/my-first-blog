from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    list_filter = ('published_date', 'author')
    search_fields = ('title', 'text')
    fields = ('title', 'author', 'text', 'image', 'published_date')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
