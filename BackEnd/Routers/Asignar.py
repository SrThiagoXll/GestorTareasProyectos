from fastapi import APIRouter,Depends,HTTPException,status
from Modelos.UsuarioSql import Asignacion
from sqlalchemy.orm import Session
from Model.AsignarTareas import AsignarBase, AsignarCreate
from DB.coneccion import SessionLocal

router = APIRouter(prefix="/Asignaciones",tags=["Asignaciones"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

@router.get("/Obtener_Asignaciones",summary="Obtener todas las Asignaciones")
async def obtener_Asignaciones(db : Session = Depends(get_db)):          
        retribuir = db.query(Asignacion).all()        
        return {"asignaciones":retribuir}

@router.get("/Obtener_Asignacion/{Asignar_ID}",summary="Obtener El Id De la Asignacion")
async def obtener_Asignacion(Asignar_ID:int, db : Session = Depends(get_db)):          
        retribuir = db.query(Asignacion).filter(Asignacion.Asignar_ID == Asignar_ID).first()
        if retribuir is None:
            raise HTTPException(status_code=404, detail="Asignacion no encontrada")
        return retribuir

@router.post("/Asignar_Tarea",status_code=status.HTTP_201_CREATED,response_model=AsignarBase,summary="Crea una nueva Retribucion")
async def Asignar_Tarea(asignar: AsignarCreate, db: Session = Depends(get_db)):    
    try:
        # 🔎 Validar que no esté asignada
        existe = db.query(Asignacion).filter(
            Asignacion.Tarea_ID == asignar.Tarea_ID,
            Asignacion.Usuario_ID == asignar.Usuario_ID
        ).first()

        if existe:
            raise HTTPException(
                status_code=400,
                detail="La tarea ya está asignada a este usuario"
            )
                       
        db_tarea = Asignacion(
            Tarea_ID = asignar.Tarea_ID,
            Usuario_ID = asignar.Usuario_ID,
            Fecha_Asignacion=asignar.Fecha_Asignacion.strftime("%Y-%m-%d"),
            Fecha_Vencimiento=asignar.Fecha_Vencimiento.strftime("%Y-%m-%d")
        )                       
                                

        db.add(db_tarea)
        db.commit()
        db.refresh(db_tarea)
        
        return db_tarea
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Asignacion No Creada. Error: {str(e)}")
       
@router.put("/Actualizar_Asignacion/{Asignar_ID}",response_model=AsignarBase,summary="Actualiza una Asignacion existente")
async def actualizar_Asignacion(Asignar_ID: int, asignar: AsignarBase, db: Session = Depends(get_db)):
    try:
        # Retrieve the existing project from the database
        db_asignar = db.query(Asignacion).filter(Asignacion.Asignar_ID == Asignar_ID).first()

        if db_asignar is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Retribucion no encontrada")

        # Update the project with the new data
        db_asignar.Asignar_ID = asignar.Asignar_ID
        db_asignar.Fecha_Asignacion = asignar.Fecha_Asignacion.strftime("%Y-%m-%d")
        db_asignar.Fecha_Vencimiento = asignar.Fecha_Vencimiento.strftime("%Y-%m-%d")
        db_asignar.Tarea_ID = asignar.Tarea_ID
        db_asignar.Usuario_ID = asignar.Usuario_ID

        # Commit the changes to the database
        db.commit()
        db.refresh(db_asignar)

        return db_asignar
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error al actualizar la Asignacion. Detalle: {str(e)}")
    
@router.delete("/Eliminar_Asignacion/{Asignar_ID}",status_code=status.HTTP_204_NO_CONTENT,summary="Elimina una Asignacion existente")
async def eliminar_Asignacion(Asignar_ID: int, db: Session = Depends(get_db)):
    try:
        # Retrieve the existing project from the database
        db_proyecto = db.query(Asignacion).filter(Asignacion.Asignar_ID == Asignar_ID).first()
        if db_proyecto is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Retibucion no encontrada")

        # Delete the project from the database
        db.delete(db_proyecto)
        db.commit()

        return {"message": "Asignacion eliminada correctamente"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error al eliminar la Asignacion. Detalle: {str(e)}")
    