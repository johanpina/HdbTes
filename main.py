from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from router.Usuario import user
from services.login import login


app = FastAPI()



app.include_router(user, prefix='/user')
app.include_router(login, prefix='/login')

@app.get("/")
def hello_world():
    return {"message": "Servidor ejecutandose"}

