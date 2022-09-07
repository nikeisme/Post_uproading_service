import bcrypt
from myposts.models import MyPost


def hash_password(password: str):
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    decode_password = hashed_password.decode("utf-8")
    return decode_password


def check_password(password: str, instance: MyPost):
    encoded_password = password.encode("utf-8")
    encoded_db_password = instance.password.encode("utf-8")
    return bcrypt.checkpw(encoded_password, encoded_db_password)