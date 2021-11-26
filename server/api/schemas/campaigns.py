from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class Campaign(BaseModel):
    id: int
    name: str
    created_at: datetime
    updated_at: datetime
    prospects_count: Optional[int]

    class Config:
        orm_mode = True


class CampaignCreate(BaseModel):
    name: str


class CampaignResponse(BaseModel):
    """One page of campaigns"""

    campaigns: List[Campaign]
    size: int
    total: int
