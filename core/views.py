from django.shortcuts import render
from blog.models import Post

# Create your views here.


def frontpageview(request):
    """
    View function for rendering the front page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered front page HTML response.
    """

    # Get all the active posts
    posts = Post.objects.filter(status=Post.ACTIVE)

    # Render the front page
    return render(request, "core/frontpage.html", {"posts": posts})


def aboutpageview(request):
    """
    Renders the about page.

    Args:
        request: The HTTP request object.

    Returns:
        The rendered about page.
    """

    # Render the about page
    return render(request, "core/about.html")
