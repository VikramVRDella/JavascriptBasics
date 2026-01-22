from fastapi import FastAPI
from database import engine,Base
import auth

app = FastAPI()
app.include_router(auth.router)

Base.metadata.create_all(engine)
