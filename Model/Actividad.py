from pydantic import BaseModel
from datetime import date

class ActividadBase(BaseModel):
    Actividad_ID:int
    Tipo_Actividad:str
    Descripción:str
    Fecha_Actividad:date
    Usuario_ID:int