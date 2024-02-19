from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Category(models.Model):
    """
    Represents a category for blog posts.
    """

    title = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ("title",)
        verbose_name_plural = "Categories"

    def __str__(self):
        return (
            self.title
        )  # Returns the title of the category as a string representation.


class Post(models.Model):
    """
    Represents a blog post.

    Attributes:
        category (Category): The category of the post.
        title (str): The title of the post.
        slug (str): The slug of the post.
        intro (str): The introduction of the post.
        body (str): The body content of the post.
        created_at (datetime): The date and time when the post was created.
        status (str): The status of the post (active or draft).
    """

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
    image = models.ImageField(upload_to="blog-post-images/", blank=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.title  # Returns the title of the post as a string representation.


class Comment(models.Model):
    """
    Represents a comment on a blog post.

    Attributes:
        post (Post): The blog post that the comment belongs to.
        name (str): The name of the commenter.
        email (str): The email address of the commenter.
        body (str): The content of the comment.
        created_at (datetime): The timestamp when the comment was created.
    """

    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)

    name = models.TextField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Dunder
    def __str__(self):
        return (
            self.name
        )  # Returns the name of the commenter as a string representation.
