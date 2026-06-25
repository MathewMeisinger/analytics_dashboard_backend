from app.auth.hashing import verify_password
from app.auth.jwt_handler import create_access_token
from app.services.user_service import get_user_by_username


def login_user(
    username: str,
    password: str,
):
    user = get_user_by_username(username)

    if not user:
        return None

    if not verify_password(
        password,
        user["password"],
    ):
        return None

    token = create_access_token(
        {
            "sub": user["username"],
            "role": user["role"],
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
    }
