from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import Response
from sqlalchemy.orm import Session
from DB.coneccion import SessionLocal
from Model.Proyecto import ProyectoBase, ProyectoCrear
from Model.Tarea import TareaBase, TareaCrear, TareaProyecto, TareaProyectoResponse, TareasResponse
from Modelos.UsuarioSql import Tarea
from Modelos.UsuarioSql import Proyecto, Usuario
from Routers.Login import get_current_user

router = APIRouter(tags=["Proyecto"], prefix="/Proyecto")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close


@router.get("/Obtener_Proyectos", summary="Obtener todos los Proyectos")
async def obtener_Proyectos(
    db: Session = Depends(get_db), #current_user: Usuario = Depends(get_current_user)
):
    proyecto = db.query(Proyecto).all()
    return {"proyecto": proyecto}


@router.get("/Obtener_Proyectos-Xml", summary="Obtener todos los Proyectos")
async def obtener_Proyectos_XML(
    db: Session = Depends(get_db), #current_user: Usuario = Depends(get_current_user)
):
    try:
        proyectos = db.query(Proyecto).all()

        # Convertir los datos a formato XML
        xml_str = "<proyectos>"
        for proyecto in proyectos:
            xml_str += f"""<proyectos><Proyecto_ID>{proyecto.Proyecto_ID}</Proyecto_ID>
                            <Nombre_Proyecto>{proyecto.Nombre_Proyecto}</Nombre_Proyecto>
                            <Descripción>{proyecto.Descripción}</Descripción>
                            <Fecha_Inicio>{proyecto.Fecha_Inicio}</Fecha_Inicio>
                            <Fecha_Final>{proyecto.Fecha_Final}</Fecha_Final>
                            <Estado_Proyecto>{proyecto.Estado_Proyecto}</Estado_Proyecto>"""
        xml_str += "</proyectos>"
        return Response(content=xml_str, media_type="application/xml")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/Obtener_Proyecto/{Proyecto_ID}", summary="Obtener El Id Del proyecto")
async def obtener_Proyecto(
    proyecto_ID: int,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user),
):
    proyecto = db.query(Proyecto).filter(Proyecto.Proyecto_ID == proyecto_ID).first()
    if proyecto is None:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    return proyecto

@router.get(
    "/Obtener_Tarea/{Proyecto_ID}/tareas",
    summary="Obtener tareas por proyecto",  
    response_model=TareasResponse
)
async def obtener_Tarea_Por_Proyecto(
    Proyecto_ID: int,
    db: Session = Depends(get_db)
):
    

    tareas = db.query(Tarea).filter(
        Tarea.Proyecto_ID == Proyecto_ID
    ).all()

    if not tareas:
        raise HTTPException(
            status_code=200,
            detail="No hay tareas para este proyecto"
        )

    # 3️⃣ Responder siempre 200
    return { "tareas": tareas}

@router.post("/{Proyecto_ID}/tarea",status_code=status.HTTP_201_CREATED,response_model=TareaProyectoResponse,summary="Crea un nueva Tarea")
async def crear_Tarea(Proyecto_ID: int, tarea: TareaProyecto, db: Session = Depends(get_db)):    
    try:
        
        proyecto = db.query(Proyecto).filter(Proyecto.Proyecto_ID == Proyecto_ID).first()
        if not proyecto:
            raise HTTPException(status_code=404, detail="Proyecto no encontrado")
                       
        db_tarea = Tarea(
            Nombre_Tarea=tarea.Nombre_Tarea,
            Descripción=tarea.Descripción,
            Fecha_Inicio=tarea.Fecha_Inicio.strftime("%Y-%m-%d"),
            Fecha_Final=tarea.Fecha_Final.strftime("%Y-%m-%d"),
            Estado_Tarea=tarea.Estado_Tarea,
            Prioridad = tarea.Prioridad,
            Proyecto_ID = Proyecto_ID)            
        db.add(db_tarea)
        db.commit()
        db.refresh(db_tarea)
        
        return db_tarea
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Tarea No Creado. Error: {str(e)}")

@router.post(
    "/Crear_Proyecto",
    status_code=status.HTTP_201_CREATED,
    response_model=ProyectoBase,
    summary="Crea un nuevo proyecto",
)
async def crear_Proyecto(
    proyecto: ProyectoCrear,
    db: Session = Depends(get_db),
    # current_user: Usuario = Depends(get_current_user),
):
    try:
        db_proyecto = Proyecto(
            Nombre_Proyecto=proyecto.Nombre_Proyecto,
            Descripción=proyecto.Descripción,
            Fecha_Inicio=proyecto.Fecha_Inicio.strftime("%Y-%m-%d"),
            Fecha_Final=proyecto.Fecha_Final.strftime("%Y-%m-%d"),
            Estado_Proyecto=proyecto.Estado_Proyecto,
        )
        db.add(db_proyecto)
        db.commit()
        db.refresh(db_proyecto)

        return db_proyecto
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Usuario No Creado. Error: {str(e)}",
        )


@router.put(
    "/Actualizar_Proyecto{Proyecto_ID}",
    response_model=ProyectoBase,
    summary="Actualiza un proyecto existente",
)
async def actualizar_Proyecto(
    Proyecto_ID: int,
    proyecto: ProyectoBase,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user),
):
    try:
        # Retrieve the existing project from the database
        db_proyecto = (
            db.query(Proyecto).filter(Proyecto.Proyecto_ID == Proyecto_ID).first()
        )

        if db_proyecto is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Proyecto no encontrado"
            )

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
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al actualizar el proyecto. Detalle: {str(e)}",
        )


@router.delete(
    "/Eliminar_Proyecto/{Proyecto_ID}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Elimina un proyecto existente",
)
async def eliminar_Proyecto(
    Proyecto_ID: int,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(get_current_user),
):
    try:
        # Retrieve the existing project from the database
        db_proyecto = (
            db.query(Proyecto).filter(Proyecto.Proyecto_ID == Proyecto_ID).first()
        )

        if db_proyecto is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Proyecto no encontrado"
            )

        # Delete the project from the database
        db.delete(db_proyecto)
        db.commit()

        return {"message": "Proyecto eliminado correctamente"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al eliminar el proyecto. Detalle: {str(e)}",
        )
