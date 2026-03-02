from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from Modelos.UsuarioSql import Asignacion, Tarea, Proyecto
from Routers.Login import get_current_user
from DB.coneccion import SessionLocal
from sqlalchemy import text

router = APIRouter(prefix="/TareaUsuario",tags=["Tarea Usuario"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get(
    "/Usuarios/{Usuario_ID}/tareas",
    summary="Obtener tareas asignadas a un usuario"
)
async def obtener_tareas_usuario(
    Usuario_ID: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    asignaciones = (
        db.query(Asignacion, Tarea, Proyecto)
        .join(Tarea, Tarea.Tarea_ID == Asignacion.Tarea_ID)
        .join(Proyecto, Proyecto.Proyecto_ID == Tarea.Proyecto_ID)
        .filter(Asignacion.Usuario_ID == Usuario_ID)
        .all()
    )

    resultado = {}

    for asignacion, tarea, proyecto in asignaciones:
        if proyecto.Proyecto_ID not in resultado:
            resultado[proyecto.Proyecto_ID] = {
                "Proyecto_ID": proyecto.Proyecto_ID,
                "Nombre_Proyecto": proyecto.Nombre_Proyecto,
                "Tareas": []
            }

        resultado[proyecto.Proyecto_ID]["Tareas"].append({
            "Tarea_ID": tarea.Tarea_ID,
            "Nombre_Tarea": tarea.Nombre_Tarea,
            "Estado_Tarea": tarea.Estado_Tarea,
            "Prioridad": tarea.Prioridad,
            "Fecha_Vencimiento": asignacion.Fecha_Vencimiento
        })

    return list(resultado.values())
