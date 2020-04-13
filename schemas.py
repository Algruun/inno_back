from datetime import datetime
from typing import List

from pydantic import BaseModel


class PizzaBase(BaseModel):
    title: str
    description: str = None


class PizzaCreate(PizzaBase):
    pass


class Pizza(PizzaBase):
    id: int
    price: float
    sku: str
    is_active: bool
    updated_at: datetime = None

    class Config:
        orm_mode = True
