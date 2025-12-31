from fastapi import APIRouter,Depends,HTTPException,status
from Modelos.UsuarioSql import Actividad
from sqlalchemy.orm import Session
from Model.Actividad import ActividadBase
from DB.coneccion import SessionLocal

router = APIRouter(default="Actividad",prefix="/Actividad")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

@router.get("/Obtener_Actividades",summary="Obtener todas las Actividades")
async def obtner_Actividades(db : Session = Depends(get_db)):          
        actividad = db.query(Actividad).all()        
        return {"actividades":actividad}

@router.get("/Obtener_Actividad{Actividad_ID}",summary="Obtener El Id De la Actividad")
async def obtner_Actividad(Actividad_ID:int, db : Session = Depends(get_db)):          
        retribuir = db.query(Actividad).filter(Actividad.Actividad_ID == Actividad_ID).first()
        if retribuir is None:
            raise HTTPException(status_code=404, detail="Actividad no encontrada")
        return retribuir

@router.post("/Crear_Actividad",status_code=status.HTTP_201_CREATED,response_model=ActividadBase,summary="Crea una nueva Actividad")
async def crear_Actividad(actividad: ActividadBase, db: Session = Depends(get_db)):    
    try:               
        db_actividad = Actividad(
            Actividad_ID=actividad.Actividad_ID,
            Tipo_Actividad=actividad.Tipo_Actividad,
            Descripción =actividad.Descripción,
            Fecha_Actividad=actividad.Fecha_Actividad.strftime("%Y-%m-%d"),
            Usuario_ID = actividad.Usuario_ID)

        db.add(db_actividad)
        db.commit()
        db.refresh(db_actividad)
        
        return db_actividad
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Actividad No Creada. Error: {str(e)}")

@router.put("/Actualizar_Actividad{Actividad_ID}",response_model=ActividadBase,summary="Actualiza una Actividad existente")
async def actualizar_Actividad(Actividad_ID: int, actividad: ActividadBase, db: Session = Depends(get_db)):
    try:
        # Retrieve the existing project from the database
        db_asignar = db.query(Actividad).filter(Actividad.Actividad_ID == Actividad_ID).first()

        if db_asignar is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Actividad no encontrada")

        # Update the project with the new data
        db_asignar.Actividad_ID = actividad.Actividad_ID
        db_asignar.Tipo_Actividad = actividad.Tipo_Actividad
        db_asignar.Descripción = actividad.Descripción
        db_asignar.Fecha_Actividad = actividad.Fecha_Actividad.strftime("%Y-%m-%d")
        db_asignar.Usuario_ID = actividad.Usuario_ID

        # Commit the changes to the database
        db.commit()
        db.refresh(db_asignar)

        return db_asignar
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error al actualizar la Actividad. Detalle: {str(e)}")
    
@router.delete("/Eliminar_Actividad/{Actividad_ID}",status_code=status.HTTP_204_NO_CONTENT,summary="Elimina una Actividad existente")
async def eliminar_Actividad(Actividad_ID: int, db: Session = Depends(get_db)):
    try:
        # Retrieve the existing project from the database
        db_proyecto = db.query(Actividad).filter(Actividad.Actividad_ID == Actividad_ID).first()

        if db_proyecto is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Actividad no encontrada")

        # Delete the project from the database
        db.delete(db_proyecto)
        db.commit()

        return {"message": "Actividad eliminado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error al eliminar la Actividad. Detalle: {str(e)}")
    