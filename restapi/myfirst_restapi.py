from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
import uvicorn

app = FastAPI()

# In-memory database
db: Dict[int, dict] = {}
current_id = 1

class Item(BaseModel):
     name: str
     description: str = ""

@app.post("/items/", response_model=Item)
def create_item(item: Item):
     global current_id
     db[current_id] = item.model_copy
     response = db[current_id].copy()
     response['id'] = current_id
     current_id += 1
     return response

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
     if item_id not in db:
          raise HTTPException(status_code=404, detail="Item not found")
     response = db[item_id].copy()
     response['id'] = item_id
     return response

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
     if item_id not in db:
          raise HTTPException(status_code=404, detail="Item not found")
     db[item_id] = item.dict()
     response = db[item_id].copy()
     response['id'] = item_id
     return response

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
     if item_id not in db:
          raise HTTPException(status_code=404, detail="Item not found")
     del db[item_id]
     return {"detail": "Item deleted"}

@app.get("/items/")
def list_items():
     return [{"id": item_id, **item} for item_id, item in db.items()]


if __name__ == "__main__":
     uvicorn.run("myfirst_restapi:app", host="127.0.0.1", port=8000, reload=True)