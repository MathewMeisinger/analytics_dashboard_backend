from datetime import datetime, timedelta, timezone
from jose import jwt
from app.config.settings import (
    JWT_SECRET_KEY,
    JWT_ALGORITHM,
    JWT_EXPIRE_MINUTES,
)


def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=JWT_EXPIRE_MINUTES
    )

    to_encode["exp"] = expire

    return jwt.encode(
        to_encode,
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM,
    )
