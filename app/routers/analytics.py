from fastapi import APIRouter, Query, Depends
from typing import List, Optional
from datetime import date
from app.models.analytics import (
    SummaryResponse, CallTypeDistribution,
    TopCaller, CallsByCity, CostByCity,
    callsByDay, callsByHour, CallRecord
    )
from app.services.analytics_service import (
    get_summary, get_call_type_distribution,
    get_top_callers, get_calls_by_city,
    get_calls_by_day, get_calls_by_hour,
    get_cost_by_city, get_call_records
    )
from app.auth.permissions import (
    require_analyst_or_admin
    )


router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)


@router.get("/summary", response_model=SummaryResponse,)
def summary(
    current_user=Depends(require_analyst_or_admin),
    city: Optional[str] = Query(default=None),
    caller_number: Optional[str] = Query(default=None),
    receiver_number: Optional[str] = Query(default=None),
    start_date: Optional[date] = Query(default=None),
    end_date: Optional[date] = Query(default=None),
):
    return get_summary(
        city=city,
        caller_number=caller_number,
        receiver_number=receiver_number,
        start_date=start_date,
        end_date=end_date,
    )


@router.get("/call-type-distribution", response_model=List[CallTypeDistribution],)
def call_type_distribution(
    current_user=Depends(require_analyst_or_admin),
    city: Optional[str] = Query(default=None),
    caller_number: Optional[str] = Query(default=None),
    receiver_number: Optional[str] = Query(default=None),
    start_date: Optional[date] = Query(default=None),
    end_date: Optional[date] = Query(default=None),
):
    return get_call_type_distribution(
        city=city,
        caller_number=caller_number,
        receiver_number=receiver_number,
        start_date=start_date,
        end_date=end_date,
    )


@router.get("/top-callers", response_model=List[TopCaller],)
def top_callers(
    current_user=Depends(require_analyst_or_admin),
    city: Optional[str] = Query(default=None),
    caller_number: Optional[str] = Query(default=None),
    receiver_number: Optional[str] = Query(default=None),
    start_date: Optional[date] = Query(default=None),
    end_date: Optional[date] = Query(default=None),
    limit: int = Query(default=10, ge=1, le=50),
):
    return get_top_callers(
        city=city,
        caller_number=caller_number,
        receiver_number=receiver_number,
        start_date=start_date,
        end_date=end_date,
        limit=limit,
    )


@router.get("/calls-by-city", response_model=List[CallsByCity],)
def calls_by_city(
    current_user=Depends(require_analyst_or_admin),
    city: Optional[str] = Query(None),
    caller_number: Optional[str] = Query(None),
    receiver_number: Optional[str] = Query(None),
    start_date: Optional[date] = Query(None),
    end_date: Optional[date] = Query(None),
):
    return get_calls_by_city(
        city=city,
        caller_number=caller_number,
        receiver_number=receiver_number,
        start_date=start_date,
        end_date=end_date,
    )


@router.get("/calls-by-hour", response_model=List[callsByHour],)
def calls_by_hour(
    current_user=Depends(require_analyst_or_admin),
    city: Optional[str] = Query(default=None),
    caller_number: Optional[str] = Query(default=None),
    receiver_number: Optional[str] = Query(default=None),
    start_date: Optional[date] = Query(default=None),
    end_date: Optional[date] = Query(default=None),
):
    return get_calls_by_hour(
        city=city,
        caller_number=caller_number,
        receiver_number=receiver_number,
        start_date=start_date,
        end_date=end_date,
    )


@router.get("/calls-by-day", response_model=List[callsByDay],)
def calls_by_day(
    current_user=Depends(require_analyst_or_admin),
    city: Optional[str] = Query(default=None),
    caller_number: Optional[str] = Query(default=None),
    receiver_number: Optional[str] = Query(default=None),
    start_date: Optional[date] = Query(default=None),
    end_date: Optional[date] = Query(default=None),
):
    return get_calls_by_day(
        city=city,
        caller_number=caller_number,
        receiver_number=receiver_number,
        start_date=start_date,
        end_date=end_date,
    )


@router.get("/cost-by-city", response_model=List[CostByCity],)
def cost_by_city(
    current_user=Depends(require_analyst_or_admin),
    city: Optional[str] = Query(default=None),
    caller_number: Optional[str] = Query(default=None),
    receiver_number: Optional[str] = Query(default=None),
    start_date: Optional[date] = Query(default=None),
    end_date: Optional[date] = Query(default=None),
):
    return get_cost_by_city(
        city=city,
        caller_number=caller_number,
        receiver_number=receiver_number,
        start_date=start_date,
        end_date=end_date,
    )


@router.get(
    "/call-records",
    response_model=List[CallRecord],
)
def call_records(
    current_user=Depends(require_analyst_or_admin),
    city: Optional[str] = Query(default=None),
    caller_number: Optional[str] = Query(default=None),
    receiver_number: Optional[str] = Query(default=None),
    start_date: Optional[date] = Query(default=None),
    end_date: Optional[date] = Query(default=None),
):

    return get_call_records(
        city=city,
        caller_number=caller_number,
        receiver_number=receiver_number,
        start_date=start_date,
        end_date=end_date,
    )
