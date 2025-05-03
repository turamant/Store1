from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session
from src.repositories.product_repo import ProductRepository
from src.schemas.product_schema import ProductCreate, ProductOut
from src.database.database import get_db
from typing import List

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/", response_model=ProductOut)
async def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    repo = ProductRepository(db)
    return repo.create(product)

@router.get("/{product_id}", response_model=ProductOut)
async def get_product(product_id: int, db: Session = Depends(get_db)):
    repo = ProductRepository(db)
    try:
        return repo.get_by_id(product_id)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Product not found")

@router.get("/", response_model=List[ProductOut])
async def get_all_products(db: Session = Depends(get_db)):
    repo = ProductRepository(db)
    return repo.get_all()