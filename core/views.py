from django.shortcuts import render
from blog.models import Post

# Create your views here.


def frontpageview(request):
    posts = Post.objects.filter(status=Post.ACTIVE)

    return render(request, "core/frontpage.html", {"posts": posts})


def aboutpageview(request):
    return render(request, "core/about.html")
