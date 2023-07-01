from django.urls import path
from blog import views


urlpatterns = [
    path('<slug:slug>/', views.blogpageview, name='blogpageview'),
]