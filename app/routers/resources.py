from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth import get_current_user
from app.db import get_db
from app.models import Shipment
from app.schemas import ShipmentIn, ShipmentOut

router = APIRouter(prefix="/shipments", tags=["shipments"])


@router.get("", response_model=list[ShipmentOut])
def list_items(db: Session = Depends(get_db), _: str = Depends(get_current_user)):
    return db.query(Shipment).order_by(Shipment.id.desc()).all()


@router.post("", response_model=ShipmentOut, status_code=status.HTTP_201_CREATED)
def create_item(body: ShipmentIn, db: Session = Depends(get_db), _: str = Depends(get_current_user)):
    row = Shipment(**body.model_dump())
    db.add(row)
    db.commit()
    db.refresh(row)
    return row


@router.get("/{item_id}", response_model=ShipmentOut)
def get_item(item_id: int, db: Session = Depends(get_db), _: str = Depends(get_current_user)):
    row = db.get(Shipment, item_id)
    if not row:
        raise HTTPException(status_code=404, detail="not found")
    return row
