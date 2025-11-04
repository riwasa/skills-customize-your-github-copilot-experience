from typing import Optional, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="FastAPI Items Example")


class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None


# In-memory "database"
_items: List[Item] = []
_next_id = 1


@app.get("/items", response_model=List[Item])
def list_items():
    return _items


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in _items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    global _next_id
    item.id = _next_id
    _next_id += 1
    _items.append(item)
    return item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated: Item):
    for i, item in enumerate(_items):
        if item.id == item_id:
            updated.id = item_id
            _items[i] = updated
            return updated
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    for i, item in enumerate(_items):
        if item.id == item_id:
            _items.pop(i)
            return
    raise HTTPException(status_code=404, detail="Item not found")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("starter-code:app", host="127.0.0.1", port=8000, reload=True)
