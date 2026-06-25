from pydantic import BaseModel, Field
from typing import Literal


class User(BaseModel):
    username: str = Field(
        min_length=3,
        max_length=50,
    )

    password: str

    role: Literal[
        "admin",
        "analyst",
    ]


class LoginRequest(BaseModel):
    username: str

    password: str


class TokenResponse(BaseModel):
    access_token: str

    token_type: str
