from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from cart_controller import get_cart, add_to_cart, remove_from_cart

app = FastAPI()

class CartItem(BaseModel):
    user_id: str
    product_id: str
    quantity: int

@app.get("/")
def read_root():
    return {"status": "Cart-service is running"}

@app.get("/cart/{user_id}")
def read_cart(user_id: str):
    return get_cart(user_id)

@app.post("/cart")
def add_item(item: CartItem):
    try:
        return add_to_cart(item.user_id, item.product_id, item.quantity)
    except Exception as e:
        import traceback
        print("❌ ERREUR INTERNE :", e)
        traceback.print_exc()
        raise HTTPException(status_code=500, detail="Erreur interne serveur")
    
@app.delete("/cart/{user_id}/{product_id}")
def delete_item(user_id: str, product_id: str):
    return remove_from_cart(user_id, product_id)
