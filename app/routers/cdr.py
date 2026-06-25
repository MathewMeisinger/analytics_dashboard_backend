from datetime import datetime
from fastapi import APIRouter, Query, HTTPException, Depends
from app.models.cdr import PaginatedCDRResponse
from app.services.cdr_service import get_paginated_cdrs
from app.auth.permissions import (
    require_analyst_or_admin
    )

router = APIRouter(
    prefix="/cdr",
    tags=["CDR"]
)


@router.get("/", response_model=PaginatedCDRResponse)
def get_cdr_records(
    current_user=Depends(require_analyst_or_admin),
    page: int = Query(
        default=1,
        ge=1,
        description="Page Number"
    ),

    limit: int = Query(
        default=10,
        ge=1,
        le=100,
        description="Records per Page"
    ),

    city: str | None = Query(
        default=None,
        description="Filter by City",
    ),

    caller_number: str | None = Query(
        default=None,
        description="Filter by Caller Number",
    ),

    receiver_number: str | None = Query(
        default=None,
        description="Filter by Receiver Number",
    ),

    start_date: datetime | None = Query(
        default=None,
        description="Start Date",
    ),

    end_date: datetime | None = Query(
        default=None,
        description="End Date",
    ),

    sort: str = Query(
        default="callStartTime",
        description="Sort Field",
    ),

    order: str = Query(
        default="desc",
        pattern="^(asc|desc)$",
        description="Sort Order",
    ),

):
    response = get_paginated_cdrs(
        page=page,
        limit=limit,
        city=city,
        caller_number=caller_number,
        receiver_number=receiver_number,
        start_date=start_date,
        end_date=end_date,
        sort=sort,
        order=order,
    )

    if response["total_records"] == 0:
        raise HTTPException(
            status_code=404,
            detail="No call records found.",
        )

    return response
