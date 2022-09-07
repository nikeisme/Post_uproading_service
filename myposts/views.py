from django.contrib.auth.hashers import check_password
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from myposts.models import MyPost
from myposts.serializers import MyPostSerializer

# Create your views here.


# 게시글 생성,조회,수정,삭제
class MyPostViewSet(viewsets.ModelViewSet):

    queryset = MyPost.objects.all().order_by("-created_at")
    serializer_class = MyPostSerializer

    def destroy(self, request, *args, **kwargs):

        try:
            password = request.data.get("password", None)
            myposts_instance = MyPost.objects.get(id=self.kwargs.get("pk"))


            # 비밀 번호 체크 함수
            if not check_password(password, myposts_instance):
                raise ValidationError("비밀번호가 맞지 않습니다.")

            return super(MyPostViewSet, self).destroy(request, *args, **kwargs)

        except MyPost.DoesNotExist as e:
            return Response(data=str(e), status=status.HTTP_404_NOT_FOUND)