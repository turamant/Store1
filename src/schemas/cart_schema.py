from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime
from typing import List, Optional

# ==== Item ====
class CartItemBase(BaseModel):
    product_id: int
    quantity: int

class CartItemOut(CartItemBase):
    id: int
    price_at_time: Decimal
    total: Decimal

    class Config:
        from_attributes = True

# ==== Cart ====
class CartBase(BaseModel):
    user_id: Optional[str] = None

class CartCreate(CartBase):
    pass

class CartOut(CartBase):
    id: int
    status: str
    created_at: datetime
    updated_at: Optional[datetime]
    items: List[CartItemOut]
    total_price: Decimal

    class Config:
        from_attributes = True