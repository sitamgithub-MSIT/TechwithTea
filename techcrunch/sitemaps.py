from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from blog.models import Post, Category


class CategorySitemap(Sitemap):
    """
    Sitemap class for generating sitemap entries for categories.
    """

    def items(self):
        """
        Returns all Category objects to be included in the sitemap.
        """
        return Category.objects.all()


class PostSitemap(Sitemap):
    """
    Sitemap class for generating sitemaps for blog posts.

    This class inherits from the base Sitemap class provided by Django.

    Attributes:
        None

    Methods:
        items(): Returns a queryset of active blog posts.
        lastmod(obj): Returns the created_at attribute of the given blog post object.
    """

    def items(self):
        return Post.objects.filter(status=Post.ACTIVE)

    def lastmod(self, obj):
        return obj.created_at
