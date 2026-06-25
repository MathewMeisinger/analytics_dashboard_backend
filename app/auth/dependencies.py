from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from jose import JWTError, jwt

from app.config.settings import (
    JWT_SECRET_KEY,
    JWT_ALGORITHM,
)

from app.services.user_service import (
    get_user_by_username,
)

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
):
    """
    Validate the JWT and return the authenticated user.
    """

    try:

        payload = jwt.decode(
            token,
            JWT_SECRET_KEY,
            algorithms=[JWT_ALGORITHM],
        )

    except JWTError:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials.",
        )

    username = payload.get("sub")

    if username is None:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials.",
        )

    user = get_user_by_username(username)

    if user is None:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found.",
        )

    return user
