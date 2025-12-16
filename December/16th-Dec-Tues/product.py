from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app=FastAPI()

class Products(BaseModel):
    id:int
    name:str
    price:float
    quantity:int


products=[
    Products(id=1,name="Pen",price=20.0,quantity=2),
    Products(id=2,name="Pencil",price=10.0,quantity=4),
    Products(id=3,name="Notebook",price=300.0,quantity=1)
]

@app.get("/products")
def get_products():
    return products

@app.get("/product/{id}")
def get_product(id:int):
    for product in products:
        if product.id == id:
            return product
    return {"Error":"Product not found"}

@app.post("/add")
def add_product(product:Products):
    products.append(product)
    return product
    