from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import JSONResponse


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/test-1")
async def test_1():
    return {"message": "Test page 1"}


@app.get("/test-2")
async def test_2():
    return {"message": "Test page 2"}


@app.post("/add-user")
async def create_item(item: Item, item_id: int):
    
    return JSONResponse({"item": item.dict(), "item_id": item_id})
