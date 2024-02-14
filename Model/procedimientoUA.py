from pydantic import BaseModel
from Model.Actividad import ActividadBase
from Model.Usuario import UsuarioBase


class UsuarioActividad():
    
    actividad:ActividadBase
    usuario:UsuarioBase