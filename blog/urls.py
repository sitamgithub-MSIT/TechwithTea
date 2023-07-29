from django.urls import path
from blog import views


urlpatterns = [
    path("<slug:category_slug>/<slug:slug>/", views.blogpageview, name="blogpageview"),
    path("<slug:slug>/", views.categorypageview, name="categorypageview"),
]