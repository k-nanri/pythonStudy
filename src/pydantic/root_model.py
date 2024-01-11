from pydantic import BaseModel, RootModel
from typing import List

class Product(BaseModel):
    id: int
    name: str
    cost: int

class Products(RootModel):
    root: List[Product]

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

print(Store.model_validate(data))