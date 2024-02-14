from pydantic import BaseModel
from datetime import date

class ComentarioBase(BaseModel):
    Comentario_ID:int
    Contenido:str
    Fecha:date
    Tarea_ID:int
    Usuario_ID:int