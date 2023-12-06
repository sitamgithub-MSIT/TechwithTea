from django.contrib import admin
from .models import Post, Comment, Category


class commentInline(admin.TabularInline):
    """
    Represents an inline form for managing comments in the admin interface.

    Attributes:
        model (Model): The model class representing the Comment model.
        raw_id_fields (list): A list of fields to be displayed as raw IDs in the form.
    """

    model = Comment
    raw_id_fields = ["post"]


class PostAdmin(admin.ModelAdmin):
    """
    Admin class for managing Post model in the blog app.

    Attributes:
        list_display (list): List of fields to display in the admin list view.
        list_filter (list): List of fields to filter the admin list view by.
        search_fields (list): List of fields to search for in the admin list view.
        inlines (list): List of inline models to display in the admin edit view.
        prepopulated_fields (dict): Dictionary of fields to automatically populate based on other fields.

    """

    list_display = ["title", "slug", "category", "created_at", "status"]
    list_filter = ["created_at", "category", "status"]
    search_fields = ["title", "body", "intro"]
    inlines = [commentInline]
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Category model.
    """

    list_display = ["title"]
    search_fields = ["title"]
    prepopulated_fields = {"slug": ("title",)}


class CommentAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing comments.
    """

    list_display = ["name", "post", "created_at"]


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
