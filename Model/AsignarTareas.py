from pydantic import BaseModel
from datetime import date 

class AsignarBase(BaseModel):
    Asignar_ID:int
    Fecha_Asignacion:date
    Fecha_Vencimiento:date
    Tarea_ID:int
    Usuario_ID:int