# oor_service.py - producer
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class OrderItem(BaseModel):
    name: str
    quantity: int
    value: float

class Order(BaseModel):
    id: int
    items: List[OrderItem]

orders_db = {
    1: Order(id=1, items=[OrderItem(name="burgera", quantity=2, value=100.0)])
}

@app.get("/orders/{order_id}", response_model=Order)
async def get_order(order_id: int):
    order = orders_db.get(order_id)
    if order:
        return order
    raise HTTPException(status_code=404, detail="Order not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
