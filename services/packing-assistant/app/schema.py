from pydantic import BaseModel
from typing import List
from datetime import date

class PacklistItem(BaseModel):
    name: str
    qty: int
    reason: str

class PacklistRequest(BaseModel):
    destination: str
    duration_days: int
    weather: str
    days: List[date]
    activities: List[str]

class PacklistResponse(BaseModel):
    destination: str
    items: List[PacklistItem]
