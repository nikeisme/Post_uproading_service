from django.db import models


class MyPost(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=10, help_text='최대 20자로 작성 해주세요')
    content = models.TextField(max_length=200, help_text='최대 200자로 작성 해주세요')
    author = models.CharField(max_length=10, help_text='최대 20자로 작성 해주세요')
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.title


