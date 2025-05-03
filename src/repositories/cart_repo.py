from sqlalchemy.orm import Session
from sqlalchemy.future import select
from src.models.cart import Cart, CartItem
from src.models.product import Product
from src.schemas.cart_schema import CartCreate

class CartRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_cart(self, data: CartCreate) -> Cart:
        cart = Cart(**data.model_dump())
        self.session.add(cart)
        self.session.commit()
        self.session.refresh(cart)
        return cart

    def get_cart_by_id(self, cart_id: int) -> Cart:
        result = self.session.execute(
            select(Cart).where(Cart.id == cart_id)
        )
        return result.scalar_one_or_none()

    def add_item(self, cart_id: int, product_id: int, quantity: int) -> CartItem:
        # Получаем продукт
        product = self.session.get(Product, product_id)
        if not product:
            raise ValueError("Product not found")

        if product.stock < quantity:
            raise ValueError(f"Not enough stock for product {product_id}")

        # Создаём элемент корзины
        item = CartItem(
            cart_id=cart_id,
            product_id=product_id,
            quantity=quantity,
            price_at_time=product.price
        )

        self.session.add(item)
        product.stock -= quantity  # блокируем остаток
        self.session.commit()
        self.session.refresh(item)
        return item

    def remove_item(self, item_id: int):
        item = self.session.get(CartItem, item_id)
        if item:
            product = self.session.get(Product, item.product_id)
            product.stock += item.quantity  # возвращаем обратно
            self.session.delete(item)
            self.session.commit()