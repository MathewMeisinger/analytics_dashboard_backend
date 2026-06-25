from datetime import datetime
from pydantic import BaseModel


class MetadataResponse(BaseModel):
    cities: list[str]
    callerNumbers: list[str]
    receiverNumbers: list[str]

    minDate: datetime
    maxDate: datetime
