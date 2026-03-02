from fastapi import APIRouter,Depends,HTTPException,status
from Modelos.UsuarioSql import SubTarea_Tarea
from sqlalchemy.orm import Session
from DB.coneccion import SessionLocal

router = APIRouter(tags=["SubTarea Tarea"],prefix="/SubTareaTareas")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/Obtener_SubTarea_Tareas",summary="Obtener todos las SubTareas")
async def obtener_SubTareas(db : Session = Depends(get_db)):          
        subtareas = db.query(SubTarea_Tarea).all()        
        return {"tareas":subtareas}

@router.get("/Obtener_SubTarea_Tarea/{SubTarea_ID}",summary="Obtener El Id De la SubTarea")
async def obtener_SubTarea(sub_tarea_id:int, db : Session = Depends(get_db)):          
        subtarea = db.query(SubTarea_Tarea).filter(SubTarea_Tarea.Tarea_ID == sub_tarea_id).first()
        if subtarea is None:
            raise HTTPException(status_code=404, detail="SubTarea no Encontrada")
        return subtarea