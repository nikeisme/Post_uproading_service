from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator


class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class MyPost(TimeStampedModel,models.Model):

    title = models.CharField(max_length=10, help_text='최대 20자로 작성 해주세요')
    content = models.TextField(max_length=200, help_text='최대 200자로 작성 해주세요')
    author = models.CharField(max_length=10, help_text='최대 20자로 작성 해주세요')
    password = models.CharField(validators=[MinLengthValidator(6, '6자 이상 적어주세요')], max_length=20,default=None, null=True)

    class Meta:
        ordering=[ '-created_at' ]
        db_table : "MyPost"


