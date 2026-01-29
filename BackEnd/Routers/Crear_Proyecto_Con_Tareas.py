from fastapi import APIRouter,Depends,HTTPException,status
from typing import Dict, Any
from sqlalchemy.orm import Session
from DB.coneccion import SessionLocal
from sqlalchemy import text
import json

router = APIRouter(prefix="/Proyecto",tags=["Proyecto"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

@router.post("/Crear_Proyecto_Tareas", status_code=status.HTTP_201_CREATED)
async def Crear_Proyecto_Tareas(
    payload: Dict[str, Any],
    db: Session = Depends(get_db)
):
    try:
        json_data = json.dumps(payload, ensure_ascii=False)

        query = text("EXEC sp_CrearProyectoConTareas_JSON :json")
        result = db.execute(query, {"json": json_data})

        proyecto_id = result.fetchone()[0]
        db.commit()

        return {
            "mensaje": "Proyecto creado correctamente",
            "Proyecto_ID": proyecto_id
        }

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
