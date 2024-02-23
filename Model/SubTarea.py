from pydantic import BaseModel
from datetime import date

class SubTareaBase(BaseModel):
    Tarea_ID: int
    Nombre_Tarea:str
    Descripción:str
    Fecha_Inicio:date
    Fecha_Final:date