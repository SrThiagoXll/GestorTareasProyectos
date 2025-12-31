from pydantic import BaseModel
from typing import Optional
class Archivo(BaseModel):
    Documento_ID: int
    Nombre:str
    Ruta:Optional[str] = None
    Tarea_ID:Optional[int] = None