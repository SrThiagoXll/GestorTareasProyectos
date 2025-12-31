from fastapi import APIRouter,Depends,HTTPException,status
from Modelos.UsuarioSql import Asignacion
from sqlalchemy.orm import Session
from Model.AsignarTareas import AsignarBase
from DB.coneccion import SessionLocal

router = APIRouter(default="Tarea",prefix="/Retribucion")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

@router.get("/Obtener_Retribuciones",summary="Obtener todas las Retribuciones")
async def obtner_Retribuciones(db : Session = Depends(get_db)):          
        retribuir = db.query(Asignacion).all()        
        return {"retribuciones":retribuir}

@router.get("/Obtener_Retribucion{Asignar_ID}",summary="Obtener El Id De la Retribucion")
async def obtner_Retribucion(Asignar_ID:int, db : Session = Depends(get_db)):          
        retribuir = db.query(Asignacion).filter(Asignacion.Asignar_ID == Asignar_ID).first()
        if retribuir is None:
            raise HTTPException(status_code=404, detail="Retribucion no encontrada")
        return retribuir

@router.post("/Crear_Retribucion",status_code=status.HTTP_201_CREATED,response_model=AsignarBase,summary="Crea una nueva Retribucion")
async def crear_Retribucion(asignar: AsignarBase, db: Session = Depends(get_db)):    
    try:               
        db_tarea = Asignacion(Asignar_ID=asignar.Asignar_ID,
                                Fecha_Asignacion=asignar.Fecha_Asignacion.strftime("%Y-%m-%d"),
                                Fecha_Final=asignar.Fecha_Vencimiento.strftime("%Y-%m-%d"),
                                Proyecto_ID = asignar.Proyecto_ID,
                                Usuario_ID = asignar.Usuario_ID)

        db.add(db_tarea)
        db.commit()
        db.refresh(db_tarea)
        
        return db_tarea
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Retribucion No Creada. Error: {str(e)}")
       
@router.put("/Actualizar_Retribucion{Asignar_ID}",response_model=AsignarBase,summary="Actualiza una Retribucion existente")
async def actualizar_Retribucion(Asignar_ID: int, asignar: AsignarBase, db: Session = Depends(get_db)):
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
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error al actualizar la Retribucion. Detalle: {str(e)}")
    
@router.delete("/Eliminar_Retribucion/{Asignar_ID}",status_code=status.HTTP_204_NO_CONTENT,summary="Elimina una Retribucion existente")
async def eliminar_Retribucion(Asignar_ID: int, db: Session = Depends(get_db)):
    try:
        # Retrieve the existing project from the database
        db_proyecto = db.query(Asignacion).filter(Asignacion.Proyecto_ID == Asignar_ID).first()

        if db_proyecto is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Retibucion no encontrada")

        # Delete the project from the database
        db.delete(db_proyecto)
        db.commit()

        return {"message": "Retribucion eliminado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error al eliminar la Retribucion. Detalle: {str(e)}")
    