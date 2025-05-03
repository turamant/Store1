from decimal import Decimal

from models.cart import Cart

class CartService:
    def __init__(self, cart_repo):
        self.cart_repo = cart_repo

    async def calculate_total(self, cart: Cart) -> Decimal:
        return sum(item.price_at_time * item.quantity for item in cart.items)