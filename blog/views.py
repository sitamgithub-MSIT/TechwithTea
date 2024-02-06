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

    # If the request is a POST request, process the comment form
    if request.method == "POST":
        form = CommentForm(request.POST)

        # If the form is valid, save the comment and redirect to the blog post
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect("blogpageview", slug=post.slug)

    else:
        form = CommentForm()

    # Render the blog post and comment form
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

    # Get the category object and all the posts belonging to the category
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=Post.ACTIVE)

    # Render the category details page
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

    # Get the search query from the request
    query = request.GET.get("query")

    # Get the posts that match the search query
    posts = Post.objects.filter(status=Post.ACTIVE).filter(
        Q(title__icontains=query) | Q(body__icontains=query) | Q(intro__icontains=query)
    )

    # Render the search results page
    return render(request, "blog/search.html", {"posts": posts, "query": query})
