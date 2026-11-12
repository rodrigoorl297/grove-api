from datetime import datetime

from pydantic import BaseModel, Field


class ShipmentIn(BaseModel):
    tracking_code: str = Field(min_length=1, max_length=120)
    origin: str
    destination: str
    status: str = "created"


class ShipmentOut(ShipmentIn):
    id: int
    created_at: datetime

    model_config = {"from_attributes": True}
