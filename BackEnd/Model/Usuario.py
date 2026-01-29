from pydantic import BaseModel,EmailStr

class UsuarioCreate(BaseModel):
    Nombre_Usuario: str
    Nombre_Completo: str
    Correo: EmailStr
    Contraseña: str
    Rol: str

class UsuarioBase(BaseModel):
    Usuario_ID: int
    Nombre_Usuario:str
    Nombre_Completo:str
    Correo:EmailStr
    Contraseña:str
    Rol:str

    model_config = {
        "from_attributes": True
    }
