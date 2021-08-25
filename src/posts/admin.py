from django.contrib import admin
from .models import Post, Comment, Like, PostImage
from sorl.thumbnail.admin import AdminImageMixin


class PostImageInline(AdminImageMixin, admin.TabularInline):
    model = PostImage


class PostAdmin(AdminImageMixin, admin.ModelAdmin):
    inlines = [PostImageInline]


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Like)