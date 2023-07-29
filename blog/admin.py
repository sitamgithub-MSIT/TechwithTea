from django.contrib import admin
from .models import Post, Comment, Category


class commentInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ["post"]


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "category", "created_at", "status"]
    list_filter = ["created_at", "category", "status"]
    search_fields = ["title", "body", "intro"]
    inlines = [commentInline]
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]
    prepopulated_fields = {"slug": ("title",)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ["name", "post", "created_at"]


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
