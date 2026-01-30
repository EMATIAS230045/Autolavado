"""
API REST para la gestión de usuarios utilizando FastAPI.
Permite crear, listar, actualizar y eliminar usuarios.
"""

from typing import List, Optional
from uuid import UUID, uuid4

from fastapi import FastAPI, HTTPException

from model import Genero, Role, Usuario

app = FastAPI()

# Base de datos simulada en memoria
usuarios_db: List[Usuario] = [
    Usuario(
        id=uuid4(),
        primer_nombre="Matias",
        apellidos="Granillo",
        genero=Genero.MASCULINO,
        roles=[Role.USER],
    ),
    Usuario(
        id=uuid4(),
        primer_nombre="dieguito",
        apellidos="Miguelito",
        genero=Genero.MASCULINO,
        roles=[Role.USER],
    ),
]


@app.get("/api/v1/users")
async def get_users(primer_nombre: Optional[str] = None) -> List[Usuario]:
    """
    Obtiene la lista de usuarios.
    Puede filtrar por nombre si se proporciona el parámetro primer_nombre.
    """
    if primer_nombre:
        resultado = [
            usuario
            for usuario in usuarios_db
            if usuario.primer_nombre.lower() == primer_nombre.lower()
        ]

        if not resultado:
            raise HTTPException(
                status_code=404,
                detail="Usuario no encontrado",
            )

        return resultado

    return usuarios_db


@app.post("/api/v1/users")
async def create_user(usuario: Usuario) -> Usuario:
    """
    Crea un nuevo usuario y lo agrega a la base de datos.
    """
    usuario.id = uuid4()
    usuarios_db.append(usuario)
    return usuario


@app.put("/api/v1/users")
async def update_user(user_id: UUID, usuario: Usuario) -> Usuario:
    """
    Actualiza la información de un usuario existente.
    """
    for index, usuario_actual in enumerate(usuarios_db):
        if usuario_actual.id == user_id:
            usuario.id = user_id
            usuarios_db[index] = usuario
            return usuario

    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado",
    )


@app.delete("/api/v1/users")
async def delete_user(user_id: UUID) -> dict:
    """
    Elimina un usuario de la base de datos.
    """
    for index, usuario in enumerate(usuarios_db):
        if usuario.id == user_id:
            usuario_eliminado = usuarios_db.pop(index)
            return {
                "message": "Usuario eliminado",
                "usuario": usuario_eliminado,
            }

    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado",
    )
