from pydantic import BaseModel


class APIResponse(BaseModel):
    success: bool
    mesage: str
