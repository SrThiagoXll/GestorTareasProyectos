from fastapi import APIRouter,Depends,HTTPException,status
from Models.UsuarioSql import SubTarea
from sqlalchemy.orm import Session
from Model.SubTarea import SubTareaBase
from DB.coneccion import SessionLocal

router = APIRouter(default="Tarea",prefix="/Tarea")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

@router.get("/Obtner_SubTareas",summary="Obtener todos las SubTareas")
async def obtner_SubTareas(db : Session = Depends(get_db)):          
        subtareas = db.query(SubTarea).all()        
        return {"subtareas":subtareas}

@router.get("/Obtner_SubTarea/{SubTarea_ID}",summary="Obtener El Id De la SubTarea")
async def obtner_SubTarea(sub_tarea_id:int, db : Session = Depends(get_db)):          
        subtarea = db.query(SubTarea).filter(SubTarea.SubTarea_ID == sub_tarea_id).first()
        if subtarea is None:
            raise HTTPException(status_code=404, detail="SubTarea no Encontrada")
        return subtarea

@router.post("/Crear_SubTarea",status_code=status.HTTP_201_CREATED,response_model=SubTareaBase,summary="Crea un nueva Tarea")
async def crear_Tarea(tarea: SubTareaBase, db: Session = Depends(get_db)):    
    try:               
        db_tarea = SubTarea(Tarea_ID=tarea.Tarea_ID,
                                Nombre_Tarea=tarea.Nombre_Tarea,
                                Descripción=tarea.Descripción,
                                Fecha_Inicio=tarea.Fecha_Inicio.strftime("%Y-%m-%d"),
                                Fecha_Final=tarea.Fecha_Final.strftime("%Y-%m-%d"),
                                )
        db.add(db_tarea)
        db.commit()
        db.refresh(db_tarea)
        
        return db_tarea
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"SubTarea No Creada. Error: {str(e)}")
       
@router.put("/Actualizar_SubTarea{SubTarea_ID}",response_model=SubTareaBase,summary="Actualiza una SubTarea existente")
async def actualizar_Tarea(sub_Tare_Id: int, subtarea: SubTareaBase, db: Session = Depends(get_db)):
    try:
        # Retrieve the existing project from the database
        db_subtarea = db.query(SubTarea).filter(SubTarea.SubTarea_ID == sub_Tare_Id).first()

        if db_subtarea is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="SubTarea no encontrado")

        # Update the project with the new data
        db_subtarea.Nombre_tarea = subtarea.Nombre_tarea
        db_subtarea.Descripción = subtarea.Descripción
        db_subtarea.Fecha_Inicio = subtarea.Fecha_Inicio.strftime("%Y-%m-%d")
        db_subtarea.Fecha_Final = subtarea.Fecha_Final.strftime("%Y-%m-%d")

        # Commit the changes to the database
        db.commit()
        db.refresh(db_subtarea)

        return db_subtarea
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error al actualizar la SubTarea. Detalle: {str(e)}")
    
@router.delete("/Eliminar_SubTarea/{SubTarea_ID}",status_code=status.HTTP_204_NO_CONTENT,summary="Elimina una SubTarea existente")
async def eliminar_Tarea(SubTarea_ID: int, db: Session = Depends(get_db)):
    try:
        # Retrieve the existing project from the database
        db_subtarea = db.query(SubTarea).filter(SubTarea.SubTarea_ID == SubTarea_ID).first()

        if db_subtarea is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="SubTarea no encontrada")

        # Delete the project from the database
        db.delete(db_subtarea)
        db.commit()

        return {"message": "SubTarea eliminada correctamente"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error al eliminar la Tarea. Detalle: {str(e)}")
    