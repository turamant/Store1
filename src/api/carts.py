from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session
from src.repositories.cart_repo import CartRepository
from src.schemas.cart_schema import CartCreate, CartOut, CartItemBase
from src.database.database import get_db

router = APIRouter(prefix="/carts", tags=["Carts"])

@router.post("/", response_model=CartOut)
async def create_cart(data: CartCreate, db: Session = Depends(get_db)):
    repo = CartRepository(db)
    cart = repo.create_cart(data)
    return cart

@router.post("/{cart_id}/items", response_model=CartOut)
async def add_item_to_cart(
    cart_id: int,
    item_data: CartItemBase,
    db: Session = Depends(get_db)
):
    repo = CartRepository(db)
    cart = repo.get_cart_by_id(cart_id)
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")

    try:
        repo.add_item(cart_id, item_data.product_id, item_data.quantity)
        cart = repo.get_cart_by_id(cart_id)
        return cart
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/items/{item_id}")
async def remove_item_from_cart(item_id: int, db: Session = Depends(get_db)):
    repo = CartRepository(db)
    repo.remove_item(item_id)
    return {"message": "Item removed"}