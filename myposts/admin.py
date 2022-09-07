from django.contrib import admin
from myposts.models import MyPost


@admin.register(MyPost)
class MyPost(admin.ModelAdmin):
    pass
