from pydantic import BaseModel
from datetime import date

class ProyectoBase(BaseModel): 
    Proyecto_ID :int 
    Nombre_Proyecto:str
    Descripción:str
    Fecha_Inicio:date
    Fecha_Final:date
    Estado_Proyecto: str # por hacer, en progreso, completado, etc.


class ProyectoCrear(BaseModel):
    
    Nombre_Proyecto:str
    Descripción:str
    Fecha_Inicio:date
    Fecha_Final:date
    Estado_Proyecto: str # por hacer, en progreso, completado, etc.
        