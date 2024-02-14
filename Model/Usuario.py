from pydantic import BaseModel

class UsuarioBase(BaseModel):
    Usuario_ID: int
    Nombre_Usuario:str
    Nombre_Completo:str
    Correo:str
    Contraseña:str
    Rol:str