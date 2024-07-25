from pydantic import BaseModel, ConfigDict, Field


class Schema(BaseModel):
    model_config = ConfigDict(from_attributes= True)


class ItemSchema(Schema):
    id: int
    name: str
    price: float = Field(ge=0)
    amount: int = Field(ge=0)


class ItemAddSchema(Schema):
    name: str
    price: float = Field(ge=0)
    amount: int = Field(ge=0)
