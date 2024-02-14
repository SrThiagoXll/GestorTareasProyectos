from pydantic import BaseModel
from datetime import date

class TareaBase(BaseModel):
    Tarea_ID: int
    Nombre_Tarea:str
    Descripción:str
    Fecha_Inicio:date
    Fecha_Final:date
    Estado_Tarea:str # por hacer, en progreso, completado, etc.
    Prioridad:str # baja, media, alta
    Proyecto_ID:int
