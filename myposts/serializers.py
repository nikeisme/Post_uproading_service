from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from myposts.models import MyPost
from myposts.utils import hash_password, check_password


class MyPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyPost
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
            "password": {"write_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True}
        }

    # password 유효성
    def validate_password(self, password: str):

        # 6자 이상
        if len(password) < 6:
            raise ValidationError("6자 이상 입력해주세요")

        # 숫자 1개 이상
        if any(pw.isdigit() for pw in password):
            return password
        else:
            raise ValidationError("숫자 1개 이상 포함해주세요.")

    # title 유효성
    def validate_title(self, title: str):

        # 20자 이상
        if len(title) > 20:
            raise ValidationError("제목은 최대 20자까지만 입력할 수 있습니다.")
        return title

    # content 유효성
    def validate_content(self, content: str):
        if len(content) > 200:
            raise ValidationError("본문은 최대 200자까지만 입력할 수 있습니다.")
        return content

    # 입력한 password 암호화 하기
    def create(self, validated_data):
        password = validated_data.pop("password", None)
        data = self.Meta.model(**validated_data)

        if password is not None:
            data.password = hash_password(password)
        data.save()

        return data


    # 암호화된 비밀번호로 게시글 수정
    def update(self, data, validated_data):
        password = validated_data.pop("password")
        if not check_password(password, instance):
            raise ValidationError("비밀번호가 틀립니다. 다시 입력해주세요.")

        data.password = hash_password(password)
        return super().update(data, validated_data)
