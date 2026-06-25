from fastapi import APIRouter, HTTPException, Depends
from app.auth.dependencies import get_current_user
from fastapi.security import OAuth2PasswordRequestForm
from app.models.user import TokenResponse

from app.services.auth_service import login_user

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/login", response_model=TokenResponse,)
def login(form_data: OAuth2PasswordRequestForm = Depends(),):
    token = login_user(
        form_data.username,
        form_data.password,
    )

    if token is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password.",
        )
    return token


@router.get("/me")
def get_me(current_user=Depends(get_current_user),):
    """
    Return the currently authenticated user.
    """

    return {
        "username": current_user["username"],
        "role": current_user["role"],
    }
