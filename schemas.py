from pydantic import BaseModel

class ItemBase(BaseModel):
    title: str
    description: str | None = None

class Item(ItemBase):
    id: int

    class Config:
        from_attributes = True 