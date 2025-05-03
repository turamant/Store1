from fastapi import FastAPI
from src.api.products import router as product_router
from src.api.carts import router as cart_router

app = FastAPI(title="E-Shop API")

@app.get("/")
def home():
    return {"message": "Welcome to E-Shop API"}

app.include_router(product_router)
app.include_router(cart_router)