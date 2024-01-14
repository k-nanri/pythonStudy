from pydantic import BaseModel, RootModel, field_validator
from typing import List

class Product(BaseModel):
    id: int
    name: str = None
    cost: int = 0

    @field_validator("name")
    @classmethod
    def check(cls, v):
        if v == "hoge":
            raise ValueError("期待する値ではない")
        return v

class Products(RootModel):
    root: List[Product]

    def __iter__(self):
        return iter(self.root)

class Store(BaseModel):
    products: Products

data = {
    "products": [
        {
            "id": 1,
            "name": "poteto",
            "cost": 100
        },
        {
            "id": 2,
            "name": "hoge",
            "cost": 500
        }
    ]
}

store = Store.model_validate(data)
print(store)