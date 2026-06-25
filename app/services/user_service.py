from app.config.database import user_collection
from app.auth.hashing import hash_password


def get_user_by_username(username: str):

    return user_collection.find_one(
        {"username": username}
    )


def create_user(
    username: str,
    password: str,
    role: str,
):

    existing_user = get_user_by_username(username)

    if existing_user:
        raise ValueError(
            "Username already exists."
        )

    user = {
        "username": username,
        "password": hash_password(password),
        "role": role,
    }

    user_collection.insert_one(user)

    return {
        "username": username,
        "role": role,
    }
