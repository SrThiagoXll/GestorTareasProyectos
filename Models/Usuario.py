from pydantic import BaseModel, Field
from typing import Optional

class Usuario(BaseModel):
    UsuarioID:Optional[int] = None
    Nombre:str = Field(default="Nombre Usuario",min_length=5,max_length=40)
    Apellido:str = Field(default="Apellido Usuario",min_length=5,max_length=40)
    Edad:int = Field(default=0,ge=0,le=100)
    Notas:int = Field(default=0,ge=0,le=100)
