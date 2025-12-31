from fastapi import APIRouter,Query,Path,status
from Modelos.Usuario import Usuario

router = APIRouter(prefix="/Usuarios")

usuarios = [

    {
        "UsuarioID":1,
        "Nombre":"Antonio",
        "Apellido":"Rivera",
        "Edad":23,
        "Notas":89
    },
    {
        "UsuarioID":2,
        "Nombre":"Andrea",
        "Apellido":"Maya",
        "Edad":25,
        "Notas":90
    },
    {
        "UsuarioID":3,
        "Nombre":"Amparo",
        "Apellido":"Zapata",
        "Edad":21,
        "Notas":96
    },
    {
        "UsuarioID":4,
        "Nombre":"Sebastian",
        "Apellido":"Usuga",
        "Edad":22,
        "Notas":87
    }
]


@router.get("/",status_code=status.HTTP_200_OK,summary="Obtener Todos los usuarios")
def obtener():
    return usuarios

@router.get("/{UsuarioID}",status_code=status.HTTP_200_OK,summary="Obtener usuario")
async def obtener_Usuario(UsuarioID:int = Path(gt=0)):
    return list(filter(lambda item: item["UsuarioID"] == UsuarioID, usuarios))

# @router.get("/",status_code=status.HTTP_200_OK,summary="Obtener Todos los usuarios")
# async def obtener_Usuario(Edad:int = Query(gt=0) ,Notas:int = Query(gt=0)):
#     return list(filter(lambda item: item["Edad"] == Edad and item["Notas"] == Notas, usuarios))

@router.post("/",status_code=status.HTTP_201_CREATED,summary="Crear un usuarios")
async def crear_usuario(usuario:Usuario):
    usuarios.append(usuario)
    return usuarios

@router.put("/{UsuarioID}",status_code=status.HTTP_202_ACCEPTED,summary="Actualizar el usuarios")
async def actualizar_Usuario(usuario:Usuario,UsuarioID:int):
    for index, item in enumerate(usuarios):
        if item["UsuarioID"] == UsuarioID:
            usuarios[index]["Nombre"] = usuario.Nombre
            usuarios[index]["Apellido"] = usuario.Apellido
            usuarios[index]["Edad"] = usuario.Edad
            usuarios[index]["Notas"] = usuario.Notas
    return usuarios

@router.delete("/{UsuarioID}",status_code=status.HTTP_204_NO_CONTENT,summary="Eliminar el usuario")
async def eliminar_Usuario(UsuarioID:int):
    for usuario in usuarios:
        if usuario["UsuarioID"] == UsuarioID:
            usuarios.remove(usuario)
    return usuarios