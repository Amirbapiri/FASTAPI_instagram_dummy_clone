from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    SECRET_KEY = "e814ac4ee28070cd3ed1e01476154be85145479bf30e589ba370a6c7800a8b1f"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    @classmethod
    def hash(cls, password):
        return pwd_context.hash(password)

    @classmethod
    def verify(cls, plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)
