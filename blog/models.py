from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ("title",)
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Post(models.Model):

    ACTIVE = "active"
    DRAFT = "draft"

    CHOICES = {
        (ACTIVE, "Active"),
        (DRAFT, "Draft"),
    }

    category = models.ForeignKey(
        Category, related_name="posts", on_delete=models.CASCADE
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=CHOICES, default=DRAFT)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)

    name = models.TextField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
