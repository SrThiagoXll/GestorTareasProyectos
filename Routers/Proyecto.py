from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.responses import Response
from Models.UsuarioSql import Proyecto
from sqlalchemy.orm import Session
from Model.Proyecto import ProyectoBase
from DB.coneccion import SessionLocal

router = APIRouter(default="Proyecto",prefix="/Proyecto")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

@router.get("/Obtner_Proyectos",summary="Obtener todos los Proyectos")
async def obtner_Proyectos(db : Session = Depends(get_db)):          
        proyecto = db.query(Proyecto).all()        
        return {"proyecto":proyecto}

@router.get("/Obtner_Proyectos-Xml",summary="Obtener todos los Proyectos")
async def obtner_Proyectos_XML(db : Session = Depends(get_db)):
        try:
            proyectos = db.query(Proyecto).all()

            # Convertir los datos a formato XML
            xml_str = "<proyectos>"
            for proyecto in proyectos:
                xml_str += (f"""<proyectos><Proyecto_ID>{proyecto.Proyecto_ID}</Proyecto_ID>
                            <Nombre_Proyecto>{proyecto.Nombre_Proyecto}</Nombre_Proyecto>
                            <Descripción>{proyecto.Descripción}</Descripción>
                            <Fecha_Inicio>{proyecto.Fecha_Inicio}</Fecha_Inicio>
                            <Fecha_Final>{proyecto.Fecha_Final}</Fecha_Final>
                            <Estado_Proyecto>{proyecto.Estado_Proyecto}</Estado_Proyecto>""")
            xml_str += "</proyectos>"       
            return Response(content=xml_str,media_type="application/xml")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

@router.get("/Obtner_Proyecto/{Proyecto_ID}",summary="Obtener El Id Del proyecto")
async def obtner_Proyecto(proyecto_ID:int, db : Session = Depends(get_db)):          
        proyecto = db.query(Proyecto).filter(Proyecto.Proyecto_ID == proyecto_ID).first()
        if proyecto is None:
            raise HTTPException(status_code=404, detail="Proyecto no encontrado")
        return proyecto

@router.post("/Crear_Proyecto",status_code=status.HTTP_201_CREATED,response_model=ProyectoBase,summary="Crea un nuevo proyecto")
async def crear_Proyecto(proyecto: ProyectoBase, db: Session = Depends(get_db)):    
    try:               
        db_proyecto = Proyecto(Proyecto_ID=proyecto.Proyecto_ID,
                                Nombre_Proyecto=proyecto.Nombre_Proyecto,
                                Descripción=proyecto.Descripción,
                                Fecha_Inicio=proyecto.Fecha_Inicio.strftime("%Y-%m-%d"),
                                Fecha_Final=proyecto.Fecha_Final.strftime("%Y-%m-%d"),
                                Estado_Proyecto=proyecto.Estado_Proyecto)
        db.add(db_proyecto)
        db.commit()
        db.refresh(db_proyecto)
        
        return db_proyecto
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Usuario No Creado. Error: {str(e)}")
       
@router.put("/Actualizar_Proyecto{Proyecto_ID}",response_model=ProyectoBase,summary="Actualiza un proyecto existente")
async def actualizar_Proyecto(Proyecto_ID: int, proyecto: ProyectoBase, db: Session = Depends(get_db)):
    try:
        # Retrieve the existing project from the database
        db_proyecto = db.query(Proyecto).filter(Proyecto.Proyecto_ID == Proyecto_ID).first()

        if db_proyecto is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Proyecto no encontrado")

        # Update the project with the new data
        db_proyecto.Nombre_Proyecto = proyecto.Nombre_Proyecto
        db_proyecto.Descripción = proyecto.Descripción
        db_proyecto.Fecha_Inicio = proyecto.Fecha_Inicio.strftime("%Y-%m-%d")
        db_proyecto.Fecha_Final = proyecto.Fecha_Final.strftime("%Y-%m-%d")
        db_proyecto.Estado_Proyecto = proyecto.Estado_Proyecto

        # Commit the changes to the database
        db.commit()
        db.refresh(db_proyecto)

        return db_proyecto
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error al actualizar el proyecto. Detalle: {str(e)}")
    
@router.delete("/Eliminar_Proyecto/{Proyecto_ID}",status_code=status.HTTP_204_NO_CONTENT,summary="Elimina un proyecto existente")
async def eliminar_Proyecto(Proyecto_ID: int, db: Session = Depends(get_db)):
    try:
        # Retrieve the existing project from the database
        db_proyecto = db.query(Proyecto).filter(Proyecto.Proyecto_ID == Proyecto_ID).first()

        if db_proyecto is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Proyecto no encontrado")

        # Delete the project from the database
        db.delete(db_proyecto)
        db.commit()

        return {"message": "Proyecto eliminado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error al eliminar el proyecto. Detalle: {str(e)}")
    