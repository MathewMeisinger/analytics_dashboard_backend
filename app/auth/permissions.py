from fastapi import (
    Depends,
    HTTPException,
    status,
)

from app.auth.dependencies import get_current_user


def require_admin(
    current_user=Depends(get_current_user),
):
    """
    Allow access to administrators only.
    """

    if current_user["role"] != "admin":

        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin privileges required.",
        )

    return current_user


def require_analyst_or_admin(
    current_user=Depends(get_current_user),
):
    """
    Allow analysts and administrators.
    """

    if current_user["role"] not in (
        "admin",
        "analyst",
    ):

        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Permission denied.",
        )

    return current_user
