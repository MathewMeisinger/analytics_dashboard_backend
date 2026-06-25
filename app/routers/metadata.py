from fastapi import APIRouter, Depends
from app.services.metadata_service import get_metadata
from app.models.metadata import MetadataResponse
from app.auth.permissions import (
    require_analyst_or_admin
    )

router = APIRouter(
    prefix="/metadata",
    tags=["Metadata"],
)


@router.get("/", response_model=MetadataResponse,)
def metadata(current_user=Depends(require_analyst_or_admin),):

    return get_metadata()
