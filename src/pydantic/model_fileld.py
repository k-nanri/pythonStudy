
from pydantic import BaseModel, model_validator
from typing import Any

class Yakiniku(BaseModel):
    beaf: str
    source: str

    @model_validator(mode="after")
    def check(self):
        print(self.beaf)
        print(self.source)


print(Yakiniku(beaf="カルビ", source="レモン"))
