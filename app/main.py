from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="QLaws Drafting Sample API")


class Item(BaseModel):
    id: int
    name: str
    description: str | None = None


# In-memory store for demo
ITEMS = [
    Item(id=1, name="Sample Law 1", description="First sample law"),
    Item(id=2, name="Sample Law 2", description="Second sample law"),
]


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/items")
def list_items():
    return ITEMS


@app.post("/items")
def create_item(item: Item):
    ITEMS.append(item)
    return item
