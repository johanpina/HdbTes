from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from router.Usuario import user

app = FastAPI()

app.include_router(user, prefix='/user')

@app.get("/")
def hello_world():
    return {"message": "Servidor ejecutandose"}