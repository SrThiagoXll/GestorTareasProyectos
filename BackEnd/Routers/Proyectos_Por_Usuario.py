from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from DB.coneccion import SessionLocal
from sqlalchemy import text

router = APIRouter(prefix="/ProyectosPorUsuario",tags=["Proyectos Por Usuario"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

@router.get("/Obtener_Proyecto_Por_Usuario/{Usuario_ID}")
async def Obtener_Proyecto_Por_Usuario(
    Usuario_ID: int,
    db: Session = Depends(get_db)
):
    try:
        query = text("""
            EXEC sp_ProyectosPorUsuario @Usuario_ID = :usuario_id
        """)

        result = db.execute(query, {"usuario_id": Usuario_ID})

        # 🔥 CLAVE: mappings()
        data = result.mappings().all()

        if not data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="El usuario no tiene proyectos asignados"
            )

        return {
            "Usuario_ID": Usuario_ID,
            "Proyectos": data
        }

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )