from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from DB.coneccion import SessionLocal
from sqlalchemy import text

router = APIRouter(prefix="/ObtenerAsignacionTarea")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

@router.get("/Obtener_Asignacion_Tarea")
async def Obtener_Asignacion_Tarea(db: Session = Depends(get_db)):

        try:

            # Ejecutar la consulta SQL "ObtenerAsignacionTarea" que devuelve ambas tablas
            query = text("EXEC ObtenerAsignacionTarea")

            results = db.execute(query)

            # Obtener los nombres de las columnas en el resultado
            column_names = results.keys()

            # Obtener la primera fila del resultado
            row = results.fetchone()

            # Crear un diccionario usando los nombres de las columnas y los valores de la fila
            data = [dict(zip(column_names, row)) for row in results.fetchall()]

            return {"ComentarioTareaUsuario": data}            
        except Exception as e:
        # Maneja las excepciones, por ejemplo, HTTP 500 para errores internos del servidor
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))