from django.urls import path
from blog import views


urlpatterns = [
    path("search/", views.search, name="search"),
    path("<slug:category_slug>/<slug:slug>/", views.blogpageview, name="blogpageview"),
    path("<slug:slug>/", views.categorypageview, name="categorypageview"),
]

"""
URL patterns for the blog application.

- The 'search/' path is used to handle search functionality.
- The '<slug:category_slug>/<slug:slug>/' path is used to display a specific blog post.
- The '<slug:slug>/' path is used to display blog posts belonging to a specific category.
"""
