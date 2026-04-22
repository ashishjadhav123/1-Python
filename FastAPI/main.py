from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    price: float

items : List[Item]= []

@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/items")
def read_items():
    return items


@app.post("/items")
def add_item(item: Item):
    items.append(item)
    return item


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    for index, existing_item in enumerate(items):
        if existing_item.id == item_id:
            items[index] = item
            return item
    return {"error": "Item not found"}


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item.id == item_id:
            del items[index]
            return {"message": "Item deleted successfully"}
    return {"error": "Item not found"}