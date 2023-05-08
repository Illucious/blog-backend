from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("post", views.posts, name='posts-page'),
    path("post/<slug:slug>", views.post_details,
         name='post-details'),    # posts/post-name

]