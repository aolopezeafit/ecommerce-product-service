from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import List
import uuid

from app.schemas.product import ProductSchema, ProductCreate, ProductUpdate
from app.services.product_service import ProductService
from app.db.session import get_db

router = APIRouter(prefix="/products", tags=["products"])

@router.post("/", response_model=ProductSchema, status_code=status.HTTP_201_CREATED)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):
    service = ProductService(db)
    return service.add_product(product)

@router.get("/", response_model=List[ProductSchema])
def list_products(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    try:
        service = ProductService(db)
        rec = service.get_all_products(skip, limit)
        return rec
    except Exception as e:
        raise e

@router.get("/{product_id}", response_model=ProductSchema)
def get_product(
    product_id: uuid.UUID,
    db: Session = Depends(get_db)
):
    service = ProductService(db)
    product = service.get_product(product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return product

@router.put("/{product_id}", response_model=ProductSchema)
def update_product(
    product_id: uuid.UUID,
    product: ProductUpdate,
    db: Session = Depends(get_db)
):
    service = ProductService(db)
    updated_product = service.update_product(product_id, product)
    if not updated_product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return updated_product

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(
    product_id: uuid.UUID,
    db: Session = Depends(get_db)
):
    service = ProductService(db)
    success = service.delete_product(product_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )