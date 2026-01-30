"""
Modelos de datos para la API de usuarios.
Incluye definiciones de enums y modelos Pydantic.
"""

from enum import Enum
from typing import List
from uuid import UUID

from pydantic import BaseModel, Field


class Genero(str, Enum):
    """
    Enum que representa el género del usuario.
    """

    MASCULINO = "Hombre"
    FEMENINO = "Mujer"
    OTRO = "Otro"


class Role(str, Enum):
    """
    Enum que representa los roles disponibles del usuario.
    """

    ADMIN = "admin"
    USER = "user"


class Usuario(BaseModel):
    """
    Modelo que representa un usuario del sistema.
    """

    id: UUID | None = Field(default=None)
    primer_nombre: str
    apellidos: str
    genero: Genero
    roles: List[Role]
