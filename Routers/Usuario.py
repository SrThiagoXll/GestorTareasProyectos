from fastapi import APIRouter, HTTPException, Depends,status
from fastapi.responses import Response
from sqlalchemy.orm import Session
from DB.coneccion import SessionLocal
from Models.UsuarioSql import Usuario
from Model.Usuario import UsuarioBase
import hashlib

router = APIRouter(default="Usuario",prefix="/Usuario")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close    

@router.get("/Obtner_Usuarios",summary="Obtener todos los usuarios")
async def obtner_Usuarios(db : Session = Depends(get_db)):          
        usuarios = db.query(Usuario).all()        
        return {"usuarios":usuarios}

@router.get("/Obtner_Usuario_Xml",summary="Obtener todos los Proyectos")
async def obtner_Usuario_XML(db : Session = Depends(get_db)):
        try:
            usuarios = db.query(Usuario).all()

            # Convertir los datos a formato XML
            xml_str = "<usuarios>"
            for usuario in usuarios:
                xml_str += (f"""<usuarios><Usuario_ID>{usuario.Usuario_ID}</Usuario_ID>
                            <Nombre_Usuario>{usuario.Nombre_Usuario}</Nombre_Usuario>
                            <Nombre_Completo>{usuario.Nombre_Completo}</Nombre_Completo>
                            <Correo>{usuario.Correo}</Correo>
                            <Contraseña>{usuario.Contraseña}</Contraseña>
                            <Rol>{usuario.Rol}</Rol></usuarios>""")
            xml_str += "</usuarios>"
            return Response(content=xml_str,media_type="application/xml")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

@router.get("/Obtner_Usuarios/{Usuario_ID}",summary="Obtener El Id del Usuario")
async def obtner_Usuario(Usuario_ID:int, db : Session = Depends(get_db)):          
        usuario = db.query(Usuario).filter(Usuario.Usuario_ID == Usuario_ID).first()
        if usuario is None:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return usuario

@router.get("/Obtner_Usuarios_xml/{Usuario_ID}",summary="Obtener El Id del Usuario")
async def obtner_Usuario_Xml(Usuario_ID:int, db : Session = Depends(get_db)):
        try:        
            usuario = db.query(Usuario).filter(Usuario.Usuario_ID == Usuario_ID).first()
            if usuario is None:
                raise HTTPException(status_code=404, detail="Usuario no encontrado")
            
            xml_str = (f"""<usuarios><Usuario_ID>{usuario.Usuario_ID}</Usuario_ID>
                                <Nombre_Usuario>{usuario.Nombre_Usuario}</Nombre_Usuario>
                                <Nombre_Completo>{usuario.Nombre_Completo}</Nombre_Completo>
                                <Correo>{usuario.Correo}</Correo>
                                <Contraseña>{usuario.Contraseña}</Contraseña>
                                <Rol>{usuario.Rol}</Rol></usuarios>""")
            return Response(content=xml_str,media_type="application/xml")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

@router.post("/Crear_Usuario",response_model=UsuarioBase,summary="Crea un nuevo usuario",status_code=status.HTTP_201_CREATED)
async def crear_Usuario(usuario: UsuarioBase, db: Session = Depends(get_db)):
    hash_password = hashlib.sha256(usuario.Contraseña.encode('utf-8')).hexdigest()
    
    db_usuario = Usuario(Usuario_ID=usuario.Usuario_ID,
                        Nombre_Usuario=usuario.Nombre_Usuario,
                        Nombre_Completo=usuario.Nombre_Completo,
                        Correo=usuario.Correo,
                        Contraseña=hash_password,
                        Rol=usuario.Rol)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario
    

@router.put("/Actualizar_usuario/{Usuario_ID}",response_model=UsuarioBase, summary="Actualiza un usuario existente")
async def actualizar_usuario(Usuario_ID: int, usuario_actualizado: UsuarioBase, db: Session = Depends(get_db)):
    db_usuario = db.query(Usuario).filter(Usuario.Usuario_ID == Usuario_ID).first() 
    
    if db_usuario:
        hash_password = hashlib.sha256(usuario_actualizado.Contraseña.encode('utf-8')).hexdigest()
        db_usuario.Nombre_Usuario = usuario_actualizado.Nombre_Usuario
        db_usuario.Nombre_Completo = usuario_actualizado.Nombre_Completo
        db_usuario.Correo = usuario_actualizado.Correo
        db_usuario.Contraseña = hash_password
        db_usuario.Rol = usuario_actualizado.Rol
        
        db.commit()
        db.refresh(db_usuario)
        return db_usuario
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    
@router.delete("/Eliminar_Proyecto/{Usuario_ID}",status_code=status.HTTP_204_NO_CONTENT,summary="Elimina un usuario existente")
async def eliminar_Proyecto(Usuario_ID: int, db: Session = Depends(get_db)):
    try:
        # Retrieve the existing project from the database
        db_usuario = db.query(Usuario).filter(Usuario.Usuario_ID == Usuario_ID).first()

        if db_usuario is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")

        # Delete the project from the database
        db.delete(db_usuario)
        db.commit()

        return {"message": "usuario eliminado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error al eliminar el proyecto. Detalle: {str(e)}")


