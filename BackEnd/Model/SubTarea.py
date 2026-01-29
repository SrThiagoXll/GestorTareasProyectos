from pydantic import BaseModel
from datetime import date

class SubTareaBase(BaseModel):
    SubTarea_ID: int
    Nombre_SubTarea:str
    Descripción:str
    Fecha_Inicio:date
    Fecha_Final:date