import bcrypt
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from .models import MyPost


# 게시글 serializer 생성
class PostingSerializer(ModelSerializer):


    class Meta:
        model = MyPost
        fields = ["id", "title", "content", "password","author", "created_at"]
        # 기타 옵션
        model = MyPost
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
            "password": {"write_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True}
        }

        def validate_password(self, password: str):

            if len(password) < 6:
                raise ValidationError("6자 이상의 비밀번호를 입력해주세요")

            if any(pw.isdigit() for pw in password):
                return password
            else:
                raise ValidationError("1개 이상의 숫자가 포함된 비밀번호를 입력해주세요")

        def validate_title(self, title: str):
            if len(title) > 20:
                raise ValidationError("제목은 최대 20자 까지만 쓸 수 있습니다.")
            return title

        def validate_content(self, content: str):
            if len(content) > 200:
                raise ValidationError("본문은 최대 200자 까지만 쓸 수 있습니다.")
            return content

    # 게시글 생성, 게시 글의 비밀 번호 암호화
    def create(self, validated_data):
        post = MyPost(**validated_data)
        password = post.password

        # utils.py
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        decoded_password = hashed_password.decode("utf-8")

        post.password = decoded_password
        post.save()
        return post

    # 게시글 수정 후, 비밀 번호 재 암호화
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key == "password":
                hashed_value = bcrypt.hashpw(value.encode("utf-8"), bcrypt.gensalt())
                decoded_password = hashed_value.decode("utf-8")

                value = decoded_password
            setattr(instance, key, value)
        instance.save()

        return instance