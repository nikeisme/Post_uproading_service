from django.urls import path, include
from rest_framework.routers import DefaultRouter

from myposts import views

router= DefaultRouter()
router.register("myposts", views.MyPostViewSet)

urlpatterns = [
    path("", include(router.urls))
]