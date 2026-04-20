from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Item(BaseModel):
    item_id: int
    price: int
    name: str

items_list = [  
Item(item_id=1, price=100, name="Item 1"),
Item(item_id=2, price=200, name="Item 2"),
Item(item_id=3, price=300, name="Item 3"),
]

class ItemUpdate(BaseModel):
    price: int
    name: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items")
def get_all_items():
    return items_list

@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items_list:
        if item.item_id == item_id:
            return item
    return {"error": "Item not found"}


@app.post("/items/")
def create_item(item: Item):
    items_list.append(item) 
    return item


# delete an item by id
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for item in items_list:
        if item.item_id == item_id:
            items_list.remove(item)
            return {"message": "Item deleted"}
    return {"error": "Item not found"}

# update an item by id
@app.put("/items/{item_id}")
def update_item(item_id: int , item_update: ItemUpdate):
    for item in items_list:
        if item.item_id == item_id:
            item.price = item_update.price
            item.name = item_update.name
            return item
    return {"error": "Item not found"}
#dfsfdsfd