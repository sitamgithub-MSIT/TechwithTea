from django.shortcuts import get_object_or_404, render
from blog.models import Post

# Create your views here.

def blogpageview(request, slug):

    post = get_object_or_404(Post, slug = slug)
    return render(request, 'blog/blogdetails.html', {'post' : post})
