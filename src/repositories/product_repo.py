from sqlalchemy import select
from sqlalchemy.orm import Session
from src.models.product import Product
from src.schemas.product_schema import ProductCreate

class ProductRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, data: ProductCreate) -> Product:
        product = Product(**data.model_dump())
        self.session.add(product)
        self.session.commit()
        self.session.refresh(product)
        return product

    def get_by_id(self, product_id: int) -> Product:
        result = self.session.execute(
            select(Product).where(Product.id == product_id)
        )
        return result.scalar_one()

    def get_all(self) -> list[Product]:
        result = self.session.execute(select(Product))
        return result.scalars().all()