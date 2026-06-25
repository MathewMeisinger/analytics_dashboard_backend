from pydantic import BaseModel, Field
from datetime import datetime


class SummaryResponse(BaseModel):
    totalCalls: int
    successfulCalls: int
    totalCost: float
    averageCost: float
    averageDuration: float
    maxDuration: int
    minDuration: int
    totalDuration: int
    successRate: float
    activeCities: int
    maxCost: float


class CallTypeDistribution(BaseModel):
    callType: str = Field(
        description="Incomming or Outgoing"
    )
    count: int = Field(
        description="Number of Calls"
    )


class TopCaller(BaseModel):
    callerNumber: str = Field(
        description="Caller Number"
    )

    totalCalls: int = Field(
        description="Total Number of Calls"
    )


class CallsByCity(BaseModel):
    city: str = Field(description="City Name")
    totalCalls: int = Field(description="Number of Calls")


class callsByHour(BaseModel):
    hour: int = Field(description="Hour of the day")
    totalCalls: int = Field(description="Number of calls")


class callsByDay(BaseModel):
    day: str = Field(description="Date")
    totalCalls: int = Field(description="Number of Calls")


class CostByCity(BaseModel):
    city: str
    averageCost: float
    totalCost: float


class CallRecord(BaseModel):
    callerName: str
    callerNumber: str
    receiverNumber: str
    city: str
    callDuration: int
    callCost: float
    callStartTime: datetime
