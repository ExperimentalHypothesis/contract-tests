# pda_service.py
from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

@app.get("/pda/orders/{order_id}")
async def get_order_from_oor(order_id: int):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"http://localhost:8000/orders/{order_id}")
            response.raise_for_status()
            return response.json()
        except Exception as e:
            raise HTTPException(status_code=404, detail="Order not found")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
