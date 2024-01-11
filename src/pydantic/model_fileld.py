
from pydantic import BaseModel, model_validator
from typing import Any

class Yakiniku(BaseModel):
    beaf: str
    source: str

    @model_validator(mode="after")
    def check(self):
        if self.beaf == "カルビ":
            if self.source == "タレ" or self.source == "レモン":
                return self
            else:
                raise ValueError("おかしな組み合わせ")
        raise ValueError("カルビ以外嫌い")


print(Yakiniku(beaf="カルビ", source="レモン"))
print(Yakiniku(beaf="カルビ", source="タレ"))
print(Yakiniku(beaf="カルビ", source="チョコ"))


