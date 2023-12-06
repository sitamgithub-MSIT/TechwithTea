from django.shortcuts import get_object_or_404, redirect, render
from blog.models import Post, Category
from .forms import CommentForm
from django.db.models import Q

# Create your views here.


def blogpageview(request, category_slug, slug):
    """
    View function for displaying a blog post and handling comments.

    Args:
        request (HttpRequest): The HTTP request object.
        category_slug (str): The slug of the blog post's category.
        slug (str): The slug of the blog post.

    Returns:
        HttpResponse: The HTTP response object containing the rendered blog post and comment form.
    """
    post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect("blogpageview", slug=post.slug)

    else:
        form = CommentForm()

    return render(request, "blog/blogdetails.html", {"post": post, "form": form})


def categorypageview(request, slug):
    """
    View function for rendering the category page.

    Args:
        request (HttpRequest): The HTTP request object.
        slug (str): The slug of the category.

    Returns:
        HttpResponse: The rendered category details page.
    """
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=Post.ACTIVE)

    return render(
        request, "blog/categorydetails.html", {"category": category, "posts": posts}
    )


def search(request):
    """
    View function to handle search functionality.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the search results.
    """
    query = request.GET.get("query")
    posts = Post.objects.filter(status=Post.ACTIVE).filter(
        Q(title__icontains=query) | Q(body__icontains=query) | Q(intro__icontains=query)
    )
    return render(request, "blog/search.html", {"posts": posts, "query": query})
