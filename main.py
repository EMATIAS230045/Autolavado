from fastapi import FastAPI
from typing import List, Optional
from uuid import UUID, uuid4
from model import Genero, Role, Usuario

app = FastAPI()
db: List[Usuario] = [ 
    Usuario(
        id=uuid4(),
        primerNombre="Edwin",
        apellidos="Cabrera Tecoralco",
        genero = Genero.masculino,  
        roles = [Role.user]
    ),
] 

@app.get("/")
async def root(): 
    return {"message": "Hello World matias"}

@app.get("/api/v1/Users")
async def fet_users():
    return db

