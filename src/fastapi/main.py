from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, PositiveInt, RootModel, ValidationError
from typing import List
from logging import getLogger, StreamHandler

logger = getLogger(__name__)
logger.addHandler(StreamHandler())
logger.setLevel("INFO")


class Product(BaseModel):
    id: int = Field(...)
    name: str = Field(...)
    cost : PositiveInt = 0

class Products(RootModel):
    root: List[Product]


app = FastAPI()

@app.get("/")
def hello():

    product = Product(id=1, name="チョコ", cost=100)
    products = Products.model_validate(product)

    return products

@app.exception_handler(ValidationError)
async def handle_validation_error(request: Request, exc: ValidationError):
    logger.info("Call Exception Handler!!")
    return JSONResponse(
        status_code=400,
        content={"message": "ValidationErrorが発生したよ"}
    )