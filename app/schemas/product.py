from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime
from decimal import Decimal
import uuid

class ProductBase(BaseModel):
    id: str = Field(..., min_length=1)
    name: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)
    price: Decimal = Field(..., gt=0, decimal_places=2)
    image_url: Optional[str] = Field(None)
    category: Optional[str] = Field(None)
    stock: Optional[int] = Field(default=0, ge=0)

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1)
    description: Optional[str] = Field(None, min_length=1)
    price: Optional[Decimal] = Field(None, gt=0, decimal_places=2)
    image_url: Optional[str] = Field(None)
    category: Optional[str] = Field(None)
    stock: Optional[int] = Field(None, ge=0)

class ProductInDB(ProductBase):
    id: str
    created_at: datetime
    updated_at: Optional[datetime]
    
    class Config:
        from_attributes = True

class ProductSchema(ProductInDB):
    pass