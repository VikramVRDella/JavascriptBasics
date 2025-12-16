from fastapi import FastAPI,Depends
from pydantic import BaseModel
from database_model import Base
import database_model
from database import engine,SessionLocal
from sqlalchemy.orm import Session

class Product(BaseModel):
    id:int
    name:str
    price:float

products=[
    Product(id=1,name="Pen",price=20.0),
    Product(id=2,name="Pencil",price=40.0)
]

Base.metadata.create_all(bind=engine)

def get_db():
    
    db=SessionLocal()

    try:
        yield db
    finally:
        db.close()


app=FastAPI()

@app.get("/products")
def get_all(db:Session=Depends(get_db)):
    db_products=db.query(database_model.Product).all()
    return db_products

@app.get("/product/{id}")
def get_by_id(id:int,db:Session=Depends(get_db)):
   db_product=db.query(database_model.Product).filter(database_model.Product.id==id).first()
   if db_product:
    return db_product
   else:
    return "Product Not Found"

@app.post("/add")
def add_product(product:Product,db:Session=Depends(get_db)):
    db.add(database_model.Product(**product.model_dump()))
    db.commit()
    return product

@app.put("/update")
def update_product(id:int,product:Product,db:Session=Depends(get_db)):
    db_product=db.query(database_model.Product).filter(database_model.Product.id == id).first()
    if db_product:
        db_product.name=product.name
        db_product.price=product.price
        db.commit()
        return "Product Updated"
    else:
       return "Product Not Found"

@app.delete("/delete")
def delete_product(id:int,product:Product,db:Session=Depends(get_db)):
   db_product=db.query(database_model.Product).filter(database_model.Product.id == id).first()
   if db_product:
      db.delete(db_product)
      db.commit()
      return "Product Deleted"
   else:
      return "Product not Found"