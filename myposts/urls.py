from django.urls import path
from myposts.views import PostsAPI, PostAPI

urlpatterns = [
    path("myposts/", PostsAPI.as_view()),
    path("myposts/<int:posting_id>/", PostAPI.as_view()),
]