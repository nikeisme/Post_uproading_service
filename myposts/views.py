from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from myposts.models import MyPost
from myposts.serializers import PostingSerializer
from myposts.pagination import PaginationHandler
from myposts.utils import hashed_password

# 페이지네이션 20개 글만 볼 수 있음


class PostPagination(PageNumberPagination):
    page_size = 20



# 게시글 전체 조회 (페이지네이션 적용)
class PostsAPI(APIView,PaginationHandler):

    pagination_class = PostPagination

    def get(self, request):
        posts = MyPost.objects.all().order_by("-created_at") # 작성 순으로 조회
        page = self.paginate_queryset(posts)
        if page is not None:
            posts_serializer = self.get_paginated_response(PostingSerializer(page, many=True).data)
        else:
            posts_serializer = PostingSerializer(posts, many=True)
        return Response(posts_serializer.data, status=status.HTTP_200_OK)

    # 게시글 작성
    def post(self, request):
        post_serializer = PostingSerializer(data=request.data)
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data, status=status.HTTP_200_OK)
        return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 게시글 1개만 조회
class PostAPI(APIView):

    # 게시글 상세 페이지
    def get(self, request, post_id):
        post = get_object_or_404(MyPost, id=post_id)
        post_serializer = PostingSerializer(post)

        return Response(post_serializer.data, status=status.HTTP_200_OK)

    # 게시글 비밀번호 입력 여부에 따른 수정
    def put(self, request, posting_id):
        post = get_object_or_404(MyPost, id=posting_id)

        input_password = request.data["password"]
        result = hashed_password(input_password, post)
        if not result:
            return Response({"message": "비밀번호가 틀렸습니다."}, status=status.HTTP_400_BAD_REQUEST)

        post_serializer = PostingSerializer(result, data=request.data, partial=True)

        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data, status=status.HTTP_200_OK)
        return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 비밀번호 입력 여부에 따른 게시글 삭제
    def delete(self, request, posting_id):
        post = get_object_or_404(MyPost, id=posting_id)

        input_password = request.data["password"]
        result = hashed_password(input_password, post)
        if result:
            result.delete()
            return Response({"message": "게시글이 삭제되었습니다."}, status=status.HTTP_200_OK)

        return Response(
            {"message": "다시 비밀번호를 입력해주세요."}, status=status.HTTP_400_BAD_REQUEST
        )