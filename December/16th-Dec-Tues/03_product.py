from fastapi import FastAPI
from pydantic import BaseModel

class Product(BaseModel):
    id:int
    name:str
    price:float

products=[
    Product(id=1,name="Pen",price=20.0),
    Product(id=2,name="Pencil",price=40.0)
]

app=FastAPI()

@app.get("/products")
def get_all():
    return products

@app.get("/product/{id}")
def get_by_id(id:int):
    for product in products:
        return product
    return {"Error":"Product not Found"}

@app.post("/add")
def add_product(product:Product):
    products.append(product)
    return product

@app.put("/update")
def update_product(id:int,product:Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product Updated Successfully"
    return "Product Update Failed"

@app.delete("/delete")
def delete_product(id:int,product:Product):
    for i in range(len(products)):
        if products[i].id==id:
            del products[i]
            return "Product Deleted Successfully"
    return "Product Not Found"