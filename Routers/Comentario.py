from fastapi import APIRouter,Depends,HTTPException,status
from Models.UsuarioSql import Comentario
from sqlalchemy.orm import Session
from Model.Comentario import ComentarioBase
from DB.coneccion import SessionLocal

router = APIRouter(default="Comentario",prefix="/Comentario")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

@router.get("/Obtener_Comentarios",summary="Obtener todas las Comentarios")
async def obtner_Comentarios(db : Session = Depends(get_db)):          
        comentario = db.query(Comentario).all()        
        return {"comentarios":comentario}

@router.get("/Obtener_comentario{Comentario_ID}",summary="Obtener El Id Del comentario")
async def obtner_Comentario(Comentario_ID:int, db : Session = Depends(get_db)):          
        retribuir = db.query(Comentario).filter(Comentario.Comentario_ID == Comentario_ID).first()
        if retribuir is None:
            raise HTTPException(status_code=404, detail="Comentario no encontrada")
        return retribuir

@router.post("/Crear_Comentario",status_code=status.HTTP_201_CREATED,response_model=ComentarioBase,summary="Crea un nuevo Comentario")
async def crear_Comentario(comentario: ComentarioBase, db: Session = Depends(get_db)):    
    try:               
        db_comentario = Comentario(Comentario_ID=comentario.Comentario_ID,
                                Contenido=comentario.Contenido,
                                Fecha=comentario.Fecha.strftime("%Y-%m-%d"),
                                Tarea_ID =comentario.Tarea_ID,
                                Usuario_ID = comentario.Usuario_ID)

        db.add(db_comentario)
        db.commit()
        db.refresh(db_comentario)
        
        return db_comentario
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Comentario No Creada. Error: {str(e)}")

@router.put("/Actualizar_Comentario{Comentario_ID}",response_model=ComentarioBase,summary="Actualiza una Comentario existente")
async def actualizar_Comentario(Comentario_ID: int, comentario: ComentarioBase, db: Session = Depends(get_db)):
    try:
        # Retrieve the existing project from the database
        db_comentario = db.query(Comentario).filter(Comentario.Comentario_ID == Comentario_ID).first()

        if db_comentario is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comentario no encontrada")

        # Update the project with the new data
        db_comentario.Comentario_ID = comentario.Comentario_ID
        db_comentario.Contenido = comentario.Contenido
        db_comentario.Fecha = comentario.Fecha.strftime("%Y-%m-%d")
        db_comentario.Tarea_ID = comentario.Tarea_ID
        db_comentario.Usuario_ID = comentario.Usuario_ID

        # Commit the changes to the database
        db.commit()
        db.refresh(db_comentario)

        return db_comentario
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error al actualizar la Comentario. Detalle: {str(e)}")
    
@router.delete("/Eliminar_Comentario/{Comentario_ID}",status_code=status.HTTP_204_NO_CONTENT,summary="Elimina una Comentario existente")
async def eliminar_Comentario(Actividad_ID: int, db: Session = Depends(get_db)):
    try:
        # Retrieve the existing project from the database
        db_proyecto = db.query(Comentario).filter(Comentario.Actividad_ID == Actividad_ID).first()

        if db_proyecto is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comentario no encontrada")

        # Delete the project from the database
        db.delete(db_proyecto)
        db.commit()

        return {"message": "Comentario eliminado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error al eliminar la Comentario. Detalle: {str(e)}")
    