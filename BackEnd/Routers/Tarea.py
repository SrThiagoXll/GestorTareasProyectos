from fastapi import APIRouter,Depends,HTTPException,status
from Modelos.UsuarioSql import Tarea
from sqlalchemy.orm import Session
from Model.Tarea import TareaBase, TareaCrear
from DB.coneccion import SessionLocal

router = APIRouter(default="Tarea",prefix="/Tarea")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

@router.get("/Obtner_Tareas",summary="Obtener todos las Tareas")
async def obtner_Tareas(db : Session = Depends(get_db)):          
        tareas = db.query(Tarea).all()        
        return {"tareas":tareas}

@router.get("/Obtner_Tarea/{Tarea_ID}",summary="Obtener El Id De la Tarea")
async def obtner_Tarea(tarea_ID:int, db : Session = Depends(get_db)):          
        tarea = db.query(Tarea).filter(Tarea.Tarea_ID == tarea_ID).first()
        if tarea is None:
            raise HTTPException(status_code=404, detail="Tarea no Encontrada")
        return tarea

@router.post("/Crear_Tarea",status_code=status.HTTP_201_CREATED,response_model=TareaBase,summary="Crea un nueva Tarea")
async def crear_Tarea(tarea: TareaCrear, db: Session = Depends(get_db)):    
    try:               
        db_tarea = Tarea(
            Nombre_Tarea=tarea.Nombre_Tarea,
            Descripción=tarea.Descripción,
            Fecha_Inicio=tarea.Fecha_Inicio.strftime("%Y-%m-%d"),
            Fecha_Final=tarea.Fecha_Final.strftime("%Y-%m-%d"),
            Estado_Tarea=tarea.Estado_Tarea,
            Prioridad = tarea.Prioridad,
            Proyecto_ID = tarea.Proyecto_ID)
        db.add(db_tarea)
        db.commit()
        db.refresh(db_tarea)
        
        return db_tarea
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Tarea No Creado. Error: {str(e)}")
       
@router.put("/Actualizar_Tarea{Tarea_ID}",response_model=TareaBase,summary="Actualiza un Tarea existente")
async def actualizar_Tarea(Tarea_ID: int, tarea: TareaCrear, db: Session = Depends(get_db)):
    try:
        # Retrieve the existing project from the database
        db_tarea = db.query(Tarea).filter(Tarea.Tarea_ID == Tarea_ID).first()

        if db_tarea is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarea no encontrado")

        # Update the project with the new data
        db_tarea.Nombre_Tarea = tarea.Nombre_Tarea
        db_tarea.Descripción = tarea.Descripción
        db_tarea.Fecha_Inicio = tarea.Fecha_Inicio.strftime("%Y-%m-%d")
        db_tarea.Fecha_Final = tarea.Fecha_Final.strftime("%Y-%m-%d")
        db_tarea.Estado_Tarea = tarea.Estado_Tarea
        db_tarea.Prioridad = tarea.Prioridad

        # Commit the changes to the database
        db.commit()
        db.refresh(db_tarea)

        return db_tarea
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error al actualizar el proyecto. Detalle: {str(e)}")
    
@router.delete("/Eliminar_Tarea/{Tarea_ID}",status_code=status.HTTP_204_NO_CONTENT,summary="Elimina un proyecto existente")
async def eliminar_Tarea(Tarea_ID: int, db: Session = Depends(get_db)):
    try:
        # Retrieve the existing project from the database
        db_tarea = db.query(Tarea).filter(Tarea.Tarea_ID == Tarea_ID).first()

        if db_tarea is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarea no encontrada")

        # Delete the project from the database
        db.delete(db_tarea)
        db.commit()

        return {"message": "Tarea eliminada correctamente"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error al eliminar la Tarea. Detalle: {str(e)}")
    