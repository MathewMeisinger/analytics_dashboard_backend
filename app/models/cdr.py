from datetime import datetime
from pydantic import BaseModel


class CDR(BaseModel):
    id: int
    callerName: str
    callerNumber: str
    receiverNumber: str
    city: str
    callDirection: bool
    callStatus: bool
    callDuration: int
    callCost: float
    callStartTime: datetime
    callEndTime: datetime


class PaginatedCDRResponse(BaseModel):
    page: int
    limit: int
    total_records: int
    total_pages: int
    records: list[CDR]
