import bcrypt

# 비밀 번호 암호화
def hashed_password(password, post):
    encoded_password = password.encode("utf-8")
    encoded_db_password = post.password.encode("utf-8")

    if not bcrypt.checkpw(encoded_password, encoded_db_password):
        return False
    return post