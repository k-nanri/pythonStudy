from datetime import datetime
from typing import Optional, Any
from pydantic import BaseModel, PositiveInt, field_validator, model_validator


class User(BaseModel):
    id: int  
    name: str = 'John Doe'
    

    @model_validator(mode='before')
    @classmethod
    def validator_name1(cls, data: Any) -> Any:
        print("Call model_validator mode is before")
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

user1 = User(**external_data)
data = user1.model_dump()
user3 = User(**data)
user2 = User.model_validate(external_data)
user4 = User.model_validate(data)
print(user1.model_dump())