from pydantic import BaseModel, RootModel
from typing import List

class Product(BaseModel):
    id: int
    name: str = None
    cost: int = 0

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
            "name": "beaf",
            "cost": 500
        }
    ]
}

store = Store.model_validate(data)
print(store)