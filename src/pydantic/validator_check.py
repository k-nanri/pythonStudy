from datetime import datetime
from typing import Optional, Any, Annotated
from pydantic import BaseModel, PositiveInt, field_validator, model_validator
from pydantic.functional_validators import AfterValidator, BeforeValidator

def plus(v: Any) -> Any:
    print("Call plus function")
    return v - 1

def double(v: Any) -> Any:
    print("Call dobule function")
    return v * 2

MyNumber = Annotated[int, AfterValidator(plus)]

class DemoModel(BaseModel):
    number: MyNumber

class User(BaseModel):
    id: int  
    name: str = 'John Doe'
    

    @model_validator(mode='before')
    @classmethod
    def validator_name1(cls, data: Any) -> Any:
        print("Call model_validator mode is before")
        print("data = " + str(data))
        return data

    @field_validator('id')
    def validate_id(cls, v):
        print("Call field_validator")
        if v < 200:
            raise AssertionError("ERROR")
        
        return v

    @model_validator(mode='after')
    def validator_name2(self) -> 'User':
        print("Call model_validator mode is after")

        return self

external_data = {
    'id': 201,
    'name': "hoge"
}

print("== Annoted Validator ==")
print(DemoModel(number="a"))

user1 = User(**external_data)